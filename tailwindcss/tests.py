from django.test import SimpleTestCase

from tailwindcss.templatetags.tailwindcss import init_tailwindcss_text


class TailwindCSSTestCase(SimpleTestCase):
    def test_init_tailwindcss_text(self):
        css_text = init_tailwindcss_text()
        self.assertIsNotNone(css_text)