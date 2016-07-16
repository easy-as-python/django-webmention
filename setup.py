import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
        readme = readme.read()

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as requirements_file:
    requirements = [line.rstrip() for line in requirements_file if line != '\n']

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-webmention',
    version='0.0.4',
    packages=find_packages(),
    description='A pluggable implementation of webmention for Django projects.',
    keywords='webmention pingback linkback blogging',
    author='Dane Hillard',
    author_email='github@danehillard.com',
    long_description=readme,
    install_requires=requirements,
    url='https://github.com/daneah/django-webmention',
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
