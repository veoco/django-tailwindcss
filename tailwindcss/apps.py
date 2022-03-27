from django.apps import AppConfig
from django.utils.autoreload import file_changed

from . import signals


class TailwindcssConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tailwindcss'

    def ready(self):
        file_changed.connect(signals.refresh_tailwindcss, dispatch_uid='tailwindcss_file_changed')
