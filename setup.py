import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-tailwindcss",
    version="0.2.2",
    author="Veoco",
    author_email="one@nomox.cn",
    description="Develop with Tailwind CSS in Django flavour.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/veoco/django-tailwindcss",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)