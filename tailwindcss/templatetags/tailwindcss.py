import re
import subprocess

from django import template
from django.conf import settings
from django.utils.safestring import mark_safe
from django.core.cache import cache


class TailwindCSS:
    def __init__(self):
        self._css_rule = re.compile(r"/.*}")
        self._cli_file = settings.TAILWINDCSS_CLI_FILE
        self._config_file = settings.TAILWINDCSS_CONFIG_FILE

    @property
    def css(self):
        tailwindcss = cache.get('tailwindcss')
        if tailwindcss:
            return tailwindcss
        else:
            self.refresh()
            return cache.get('tailwindcss')

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
def tailwindcss():
    css = mark_safe("<style>{}</style>".format(tailwind.css))
    return css
