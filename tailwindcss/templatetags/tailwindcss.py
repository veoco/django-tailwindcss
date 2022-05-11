import re
import subprocess

from django import template
from django.conf import settings
from django.utils.safestring import mark_safe
from django.core.cache import cache


class TailwindCSS:
    def __init__(self):
        self._css_rule = re.compile(r"/.*}")
        self._bare_css_rule = re.compile(r"sepia: }(.*)")
        self._base_dir = settings.BASE_DIR
        self._cli_file = settings.TAILWINDCSS_CLI_FILE
        self._config_file = settings.TAILWINDCSS_CONFIG_FILE
    
    def get_css(self, template_path='', bare=False):
        if template_path:
            cache_key = '/'.join(('tailwindcss', template_path))
            path = self._base_dir / template_path
        else:
            cache_key = 'tailwindcss'
            path = ''

        tailwindcss = cache.get(cache_key)
        if not tailwindcss:
            self.refresh(path)
            tailwindcss = cache.get(cache_key)

        if bare:
            return self._bare_css_rule.search(tailwindcss).group(1)
        return tailwindcss

    def refresh(self, path=''):
        if path:
            cache_key = 'tw/' + str(path)
            task_args = (self._cli_file, "-m", "-c", self._config_file, "--content", path)
        else:
            cache_key = 'tailwindcss'
            task_args = (self._cli_file, "-m", "-c", self._config_file)

        task = subprocess.run(
            task_args,
            capture_output=True,
            text=True,
            check=True,
        )
        tailwindcss = self._css_rule.search(task.stdout).group()
        cache.set(cache_key, tailwindcss, timeout=None)


tailwind = TailwindCSS()

register = template.Library()


@register.simple_tag
def tailwindcss(template_path='', raw=False, bare=False):
    css = tailwind.get_css(template_path, bare)
    if raw:
        return mark_safe(css)
    return mark_safe("<style>{}</style>".format(css))


@register.simple_tag
def raw_tailwindcss(template_path='', raw=True, bare=False):
    return tailwindcss(template_path, raw, bare)


@register.simple_tag
def bare_tailwindcss(template_path='', raw=True, bare=True):
    return tailwindcss(template_path, raw, bare)
