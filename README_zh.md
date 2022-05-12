[English](README_zh.md) | 中文

# django-tailwindcss

[![Django CI](https://github.com/veoco/django-tailwindcss/actions/workflows/django.yml/badge.svg)](https://github.com/veoco/django-tailwindcss/actions/workflows/django.yml)

使用 Tailwind CSS 开发项目，Django 风味。


## 快速开始

### 1. 从 pip 安装 django-tailwindcss

```
pip install django-tailwindcss
```

### 2. 下载 Tailwind CSS CLI 文件并创建 tailwind.config.js

CLI 文件下载地址 [https://github.com/tailwindlabs/tailwindcss/releases](https://github.com/tailwindlabs/tailwindcss/releases)

`tailwind.config.js` 可以在这找到 [https://tailwindcss.com/docs/installation](https://tailwindcss.com/docs/installation)

例如：

```
module.exports = {
  content: ["./**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

将 `tailwindcss-linux-x64` （用于 linux）和 `tailwind.config.js` 放在 `manage.py`相同的目录。

你的项目 `proj` 应该像这样：

```
proj
├── proj
│   └── settings.py
├── manage.py
├── tailwindcss-linux-x64
└── tailwind.config.js
```

### 3. 添加 tailwindcss 到你的 settings.INSTALLED_APPS

```python
INSTALLED_APPS = [
    ...
    "tailwindcss",
    ...
]
```

### 4. 在你的 settings 中添加这些变量

```python
# BASE_DIR = Path(__file__).resolve().parent

TAILWINDCSS_CLI_FILE = BASE_DIR / 'tailwindcss-linux-x64'
TAILWINDCSS_CONFIG_FILE = BASE_DIR / 'tailwind.config.js'
# 用于文件模式
TAILWINDCSS_OUTPUT_FILE = 'style.css'
```

### 5. 在你的基础模板中添加 tailwindcss 标签

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

### 6. (可选) 生成 tailwindcss 文件

使用 `maketailwindcss` 命令在 `Path(settings.STATIC_ROOT) / settings.TAILWINDCSS_OUTPUT_FILE` 生成 tailwindcss 文件。

```
python manage.py maketailwindcss
```

`{% tailwindcss %}` 的输出将变为使用文件。

## 缓存

`django-tailwindcss` 生成 CSS 的步骤被推迟，直到首次访问使用了 `tailwindcss` 标签的页面。生成的 CSS 被保存在缓存中，以加快页面的加载，防止阻塞 Django 进程，对于修改后重新加载的 CSS 仍然需要等待一段时间才会自动生效。

这在使用默认的 `LocMemCache` 缓存后端时配合的很好，但当使用 `DummyCache` 后端会退化到 0.3.0 之前版本的状态，因为此后端根本就没有缓存。

需要注意使用 `Memcached`、`Redis`、`DatabaseCache`、`FileBasedCache` 缓存后端时，缓存不会像 `LocMemCache` 后端因为进程重启而自动清空，因此可能导致在更新文件后使用过时的 CSS，为此新增了 `refreshtailwindcss` 管理命令，便于手动刷新缓存：

```
python manage.py refreshtailwindcss 
```


## 内部

`django-tailwindcss` 在 Django 每次启动 **和** 文件发生变化时生成 CSS。

`{% tailwindcss %}` 的输出总是如:

```html
<style>/*! tailwindcss v3.0.23 | MIT License | https://tailwindcss.com*/*,:after,:before{border:0 solid #e5e7eb;box-sizing:border-box}...</style>
```

所以你通常只需要添加一次这个标签。

如果你添加了 `raw` 参数，如 `{% tailwindcss raw=True %}`。输出将如：

```html
/*! tailwindcss v3.0.23 | MIT License | https://tailwindcss.com*/*,:after,:before{border:0 solid #e5e7eb;box-sizing:border-box}...
```

如果你生成了 tailwindcss 文件，输出将如：

```html
<link rel="stylesheet" type="text/css" href="...">
```
