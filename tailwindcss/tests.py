from django.test import SimpleTestCase

from tailwindcss.templatetags.tailwindcss import tailwind


class TailwindCSSTestCase(SimpleTestCase):
    def test_init_tailwindcss_text(self):
        css_text = tailwind.get_css()
        self.assertIsNotNone(css_text)

    def test_bare_tailwindcss_text(self):
        css_text = tailwind.get_css(bare=True)
        self.assertIsNotNone(css_text)
        self.assertNotIn('sepia:', css_text)