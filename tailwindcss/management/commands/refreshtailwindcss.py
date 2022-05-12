from django.core.management.base import BaseCommand

from tailwindcss.templatetags.tailwindcss import tailwind


class Command(BaseCommand):
    help = 'Refresh tailwindcss cache'

    def handle(self, *args, **options):
        tailwind.refresh()
        self.stdout.write(self.style.SUCCESS('Successfully refresh tailwindcss cache'))