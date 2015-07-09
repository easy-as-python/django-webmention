import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
        README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-webmention',
    version='0.0.1',
    packages=find_packages(),
    description='A pluggable implementation of webmention for Django projects.',
    author='Dane Hillard',
    author_email='github@danehillard.com',
    long_description=README,
    url='https://github.com/daneah/django-webmention',
)
