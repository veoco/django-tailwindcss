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
        self._output_file = Path(settings.TAILWINDCSS_OUTPUT_FILE)

        self.css_url = ''

        if self._output_file.is_file():
            self.css_url = static(self._output_file)

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
def tailwindcss(raw=False):
    if tailwind.css_url:
        return tailwind.css_url
    if raw:
        return mark_safe(tailwind.css)
    return mark_safe("<style>{}</style>".format(tailwind.css))
