from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

SECRET_KEY = 'fake-key'

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    "tests",
    "tailwindcss",
]

ROOT_URLCONF = 'tests.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
    }
]

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'static'

TAILWINDCSS_CLI_FILE = BASE_DIR / 'tailwindcss-linux-x64'

TAILWINDCSS_CONFIG_FILE = BASE_DIR / 'tailwind.config.js'

TAILWINDCSS_OUTPUT_FILE = 'style.css'
