from django.test import SimpleTestCase

from tailwindcss.templatetags.tailwindcss import tailwind


class TailwindCSSTestCase(SimpleTestCase):
    def test_init_tailwindcss_text(self):
        css_text = tailwind.css
        self.assertIsNotNone(css_text)