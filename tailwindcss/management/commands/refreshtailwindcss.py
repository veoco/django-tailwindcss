import os

from django.core.management.base import BaseCommand
from django.conf import settings
from django.template.utils import get_app_template_dirs
from django.core.cache import cache

from tailwindcss.templatetags.tailwindcss import tailwind


class Command(BaseCommand):
    help = 'Refresh tailwindcss cache'

    def handle(self, *args, **options):
        tailwind.refresh()
        self.stdout.write(self.style.NOTICE('total css refreshed'))

        template_dir_list = []
        for template_dir in get_app_template_dirs('templates'):
            if settings.ROOT_DIR in template_dir:
                template_dir_list.append(template_dir)


        template_dirs = get_app_template_dirs('templates')
        if settings.TEMPLATES:
            template_backend = settings.TEMPLATES[0]
            template_backend_name = template_backend.get('BACKEND')
            template_extra_dirs = template_backend.get('DIRS')
            if template_extra_dirs and template_backend_name == 'django.template.backends.django.DjangoTemplates':
                template_dirs += template_extra_dirs

        for template_dir in template_dirs:
            for base_dir, dirnames, filenames in os.walk(template_dir):
                for filename in filenames:
                    path = os.path.join(base_dir, filename)
                    cache_key = 'tw/' + path
                    
                    tailwindcss = cache.get(cache_key)
                    if tailwindcss:
                        tailwind.refresh(path)
                        self.stdout.write(self.style.NOTICE('{} refreshed'.format(path)))

        self.stdout.write(self.style.SUCCESS('Successfully refresh tailwindcss cache'))