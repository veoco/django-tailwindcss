[English](README_zh.md) | 中文

# django-tailwindcss

使用 Tailwind CSS 开发项目，Django 风味。


## Quick Start

### 1. 从 pip 安装 `django-tailwindcss`

```
pip install django-tailwindcss
```

### 2. 下载 Tailwind CSS CLI 文件并创建 `tailwind.config.js`：

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

### 3. 添加 `tailwindcss` 到你的 settings.INSTALLED_APPS：

```python
INSTALLED_APPS = [
    ...
    "tailwindcss",
    ...
]
```

### 4. 在你的 settings 中添加这些变量:

```python
# BASE_DIR = Path(__file__).resolve().parent

TAILWINDCSS_CLI_FILE = BASE_DIR / 'tailwindcss-linux-x64'
TAILWINDCSS_CONFIG_FILE = BASE_DIR / 'tailwind.config.js'
```

### 5. 在你的基础模板中添加 `tailwindcss` 标签：

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


## 内部

`django-tailwindcss` 在 Django 每次启动 **和** 文件发生变化时生成 CSS。

`{% tailwindcss %}` 的输出总是:

```html
<style>/*! tailwindcss v3.0.23 | MIT License | https://tailwindcss.com*/*,:after,:before{border:0 solid #e5e7eb;box-sizing:border-box}...</style>
```

所以你通常只需要添加一次这个标签。
