from tailwindcss.templatetags.tailwindcss import tailwind


def refresh_tailwindcss(sender, **kwargs):
    tailwind.refresh()