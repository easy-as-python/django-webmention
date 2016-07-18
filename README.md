# django-webmention [![PyPI version](https://badge.fury.io/py/django-webmention.svg)](https://badge.fury.io/py/django-webmention) [![Build Status](https://travis-ci.org/easy-as-python/django-webmention.svg?branch=master)](https://travis-ci.org/easy-as-python/django-webmention)

[webmention](https://www.w3.org/TR/webmention/) for Django projects.

## Installation

`$ pip install django-webmention`

* Add `webmention` to `INSTALLED_APPS`
* Run `manage.py migrate webmention`
* Add `url(r'^webmention', include('webmention.urls', namespace='webmention'))` to top-level `urls.py`
* Run `manage.py test webmention` to ensure unit tests all pass 

## Usage

* Include webmention information by either:
    * Adding `webmention.middleware.WebMentionMiddleware` to `MIDDLEWARE_CLASSES` (affects all views)
    * Decorating a specific view with `webmention.middleware.include_webmention_information`
* View webmention responses in the Django admin tool and mark them as reviewed as needed
