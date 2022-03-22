import re
import subprocess

from django import template
from django.conf import settings
from django.utils.html import format_html


class TailwindCSS:
    def __init__(self):
        self.css = None
        self._css_rule = re.compile(r"/.*}")
        self._cli_file = settings.TAILWINDCSS_CLI_FILE
        self._config_file = settings.TAILWINDCSS_CONFIG_FILE

        self.refresh()

    def refresh(self):
        task = subprocess.run(
            [self._cli_file, "-m", "-c", self._config_file],
            capture_output=True,
            text=True,
            check=True,
        )
        self.css = self._css_rule.search(task.stdout).group()


tailwind = TailwindCSS()

register = template.Library()


@register.simple_tag
def tailwindcss():
    css = format_html("<style>{}</style>", tailwind.css)
    return css
