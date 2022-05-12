from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from tailwindcss.templatetags.tailwindcss import tailwind


class Command(BaseCommand):
    help = 'Generate tailwindcss file'

    def handle(self, *args, **options):
        css = tailwind.css
        filepath = Path(settings.STATIC_ROOT) / settings.TAILWINDCSS_OUTPUT_FILE
        with open(filepath, 'w') as f:
            f.write(css)
        self.stdout.write(self.style.SUCCESS('Successfully generated tailwindcss file'))