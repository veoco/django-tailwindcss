from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

SECRET_KEY = 'fake-key'

INSTALLED_APPS = [
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

TAILWINDCSS_CLI_FILE = BASE_DIR / 'tailwindcss-linux-x64'

TAILWINDCSS_CONFIG_FILE = BASE_DIR / 'tailwind.config.js'