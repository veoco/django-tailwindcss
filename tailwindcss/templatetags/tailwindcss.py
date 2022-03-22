import re
import subprocess

from django import template
from django.conf import settings
from django.utils.html import format_html


register = template.Library()

CSS_RULE = re.compile(r'/.*}')


def init_tailwindcss_text():
    tailwindcss_cli_file = settings.TAILWINDCSS_CLI_FILE
    tailwindcss_config_file = settings.TAILWINDCSS_CONFIG_FILE
    task = subprocess.run(
        [tailwindcss_cli_file, "-m", "-c", tailwindcss_config_file],
        capture_output=True,
        text=True,
        check=True,
    )
    css_text = CSS_RULE.search(task.stdout)
    return css_text.group()


tailwindcss_text = init_tailwindcss_text()


@register.simple_tag
def tailwindcss():
    css = format_html('<style>{}</style>', tailwindcss_text)
    return css
