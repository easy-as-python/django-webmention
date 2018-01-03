# django-webmention [![PyPI version](https://badge.fury.io/py/django-webmention.svg)](https://badge.fury.io/py/django-webmention) [![Build Status](https://travis-ci.org/easy-as-python/django-webmention.svg?branch=master)](https://travis-ci.org/easy-as-python/django-webmention)

[webmention](https://www.w3.org/TR/webmention/) for Django projects.

## Installation

`$ pip install django-webmention`

* Add `webmention` to `INSTALLED_APPS`
* Run `manage.py migrate webmention`
* Add `url(r'^webmention', include('webmention.urls', namespace='webmention'))` to top-level `urls.py`
    * Use `path('webmention/', include(webmention.urls))` for newer projects
* Run `manage.py test webmention` to ensure unit tests all pass 

## Usage

* Include webmention information by either:
    * Installing the middleware in `settings.py` (affects all views)
        * Use `webmention.middleware.webmention_middleware` in `MIDDLEWARE` for new projects and projects with Django >= 1.10
        * Use `webmention.middleware.WebMentionMiddleware` in `MIDDLEWARE_CLASSES` for older projects
    * Decorating a specific view with `webmention.middleware.include_webmention_information`
* View webmention responses in the Django admin tool and mark them as reviewed as needed
