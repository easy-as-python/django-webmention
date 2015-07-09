import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
        readme = readme.read()

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as requirements_file:
    requirements = [line.rstrip() for line in requirements_file if line != '\n']

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-webmention',
    version='0.0.1',
    packages=find_packages(),
    description='A pluggable implementation of webmention for Django projects.',
    author='Dane Hillard',
    author_email='github@danehillard.com',
    long_description=readme,
    install_requires=requirements,
    url='https://github.com/daneah/django-webmention',
)
