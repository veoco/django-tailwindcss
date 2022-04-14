English | [中文](README_zh.md)

# django-tailwindcss

[![Django CI](https://github.com/veoco/django-tailwindcss/actions/workflows/django.yml/badge.svg)](https://github.com/veoco/django-tailwindcss/actions/workflows/django.yml)

Develop with Tailwind CSS in Django flavour.


## Quick Start

### 1. Install django-tailwindcss from pip

```
pip install django-tailwindcss
```

### 2. Download Tailwind CSS CLI file and create tailwind.config.js

CLI file can be download from [https://github.com/tailwindlabs/tailwindcss/releases](https://github.com/tailwindlabs/tailwindcss/releases)

`tailwind.config.js` can be found at [https://tailwindcss.com/docs/installation](https://tailwindcss.com/docs/installation)

Example:

```
module.exports = {
  content: ["./**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

Store `tailwindcss-linux-x64` (for linux) and `tailwind.config.js` at the same directory of `manage.py`.

And your project `proj` should be like:

```
proj
├── proj
│   └── settings.py
├── manage.py
├── tailwindcss-linux-x64
└── tailwind.config.js
```

### 3. Add tailwindcss to your settings.INSTALLED_APPS

```python
INSTALLED_APPS = [
    ...
    "tailwindcss",
    ...
]
```

### 4. Create these variables in your settings

```python
# BASE_DIR = Path(__file__).resolve().parent

TAILWINDCSS_CLI_FILE = BASE_DIR / 'tailwindcss-linux-x64'
TAILWINDCSS_CONFIG_FILE = BASE_DIR / 'tailwind.config.js'
```

### 5. Use tailwindcss tag in your base template

```html
{% load tailwindcss %}
<html>
  <head>
    ...
    {% tailwindcss %}
    ...
  </head>
  ...
</html>
```

## Cache

`django-tailwindcss` CSS generation step is deferred until the first visit to a page that uses the `tailwindcss` tag. The generated CSS is stored in the cache to speed up page loading and prevent blocking the Django process, and for modified and reloaded CSS there is still a waiting period before it takes effect automatically.

This works well with the default `LocMemCache` caching backend, but when using the `DummyCache` backend it degrades to a pre-0.3.0 state, as this backend has no cache at all.

Note that when using the `Memcached`, `Redis`, `DatabaseCache`, `FileBasedCache` caching backends, the cache is not automatically cleared as the `LocMemCache` backend is when the process is restarted, so this may result in out-of-date CSS being used after updating a file, for which the `refreshtailwindcss` management command has been added to facilitate manual refreshing of the cache.

```
python manage.py refreshtailwindcss 
```

## Internal

`django-tailwindcss` generates CSS each time django startup **and** file changes.

And `{% tailwindcss %}` outputs are same as:

```html
<style>/*! tailwindcss v3.0.23 | MIT License | https://tailwindcss.com*/*,:after,:before{border:0 solid #e5e7eb;box-sizing:border-box}...</style>
```

So you usually only need to add it once.
