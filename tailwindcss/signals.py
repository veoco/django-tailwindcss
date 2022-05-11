from django.core.cache import cache

from tailwindcss.templatetags.tailwindcss import tailwind


def refresh_tailwindcss(sender, **kwargs):
    path = kwargs.get('file_path')
    cache_key = 'tw/' + str(path)

    tailwindcss = cache.get(cache_key)
    if tailwindcss:
        tailwind.refresh(path)
    else:
        tailwind.refresh()