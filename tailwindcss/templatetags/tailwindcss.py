import re
import subprocess

from pathlib import Path

from django import template
from django.conf import settings
from django.utils.safestring import mark_safe
from django.core.cache import cache
from django.templatetags.static import static


class TailwindCSS:
    def __init__(self):
        self._css_rule = re.compile(r"/.*}")
        self._cli_file = settings.TAILWINDCSS_CLI_FILE
        self._config_file = settings.TAILWINDCSS_CONFIG_FILE
        self._output_file = settings.TAILWINDCSS_OUTPUT_FILE

        self._output_filepath = Path(settings.STATIC_ROOT) / settings.TAILWINDCSS_OUTPUT_FILE
        self._is_output_filepath = self._output_filepath.is_file()

    @property
    def css(self):
        tailwindcss = cache.get('tailwindcss')
        if tailwindcss:
            return tailwindcss
        else:
            self.refresh()
            return cache.get('tailwindcss')
    
    @property
    def css_url(self):
        if self._is_output_filepath:
            return static(self._output_file)
        return ''

    def refresh(self):
        task = subprocess.run(
            [self._cli_file, "-m", "-c", self._config_file],
            capture_output=True,
            text=True,
            check=True,
        )
        tailwindcss = self._css_rule.search(task.stdout).group()
        cache.set('tailwindcss', tailwindcss, timeout=None)


tailwind = TailwindCSS()

register = template.Library()


@register.simple_tag
def tailwindcss(raw=False):
    if raw:
        return mark_safe(tailwind.css)
    if tailwind.css_url:
        return mark_safe('<link rel="stylesheet" type="text/css" href="{}">'.format(tailwind.css_url))
    return mark_safe("<style>{}</style>".format(tailwind.css))
