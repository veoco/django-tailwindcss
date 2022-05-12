from io import StringIO

from django.conf import settings
from django.core.management import call_command
from django.test import SimpleTestCase

from tailwindcss.templatetags.tailwindcss import tailwind


class TailwindCSSTestCase(SimpleTestCase):
    def test_init_tailwindcss_text(self):
        css_text = tailwind.css
        self.assertIsNotNone(css_text)
    
    def test_generate_file(self):
        out = StringIO()
        call_command('generatetailwindcss', stdout=out)

        filepath = settings.STATIC_ROOT / settings.TAILWINDCSS_OUTPUT_FILE
        self.assertTrue(filepath.is_file(), 'File not generate')

        self.assertIn('Successfully generated tailwindcss file', out.getvalue(), 'Generate file command error')

        filepath.unlink()
        self.assertFalse(filepath.is_file(), 'File not delete')
