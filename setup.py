from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="password_generator",
    version="0.1",
    author="Igor Cruz",
    author_email="igorrvbc@gmail.com",
    description="Gerador de simples de senhas.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/igorrvbc/simple-package-template",
    packages=find_packages(),
    classifiers=[
        'Programing Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.6',
)