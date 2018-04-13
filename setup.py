import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
        readme = readme.read()

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as requirements_file:
    requirements = [line.rstrip() for line in requirements_file if line != '\n']

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-webmention',
    version='1.0.0',
    packages=find_packages(),
    description='A pluggable implementation of webmention for Django projects.',
    author='Dane Hillard',
    author_email='github@danehillard.com',
    long_description=readme,
    install_requires=requirements,
    url='https://github.com/easy-as-python/django-webmention',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
