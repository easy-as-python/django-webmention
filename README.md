# django-webmention [![PyPI version](https://badge.fury.io/py/django-webmention.svg)](https://badge.fury.io/py/django-webmention) [![Build Status](https://travis-ci.org/easy-as-python/django-webmention.svg?branch=master)](https://travis-ci.org/easy-as-python/django-webmention)

[webmention](https://www.w3.org/TR/webmention/) for Django projects.

## Installation

`$ pip install django-webmention`

* Add `'webmention'` to `INSTALLED_APPS`
* Run `python manage.py migrate webmention`
* Add the URL patterns to your top-level `urls.py`
    * `path('webmention/', include(webmention.urls))` for Django >= 2.0
    * `url(r'^webmention', include('webmention.urls', namespace='webmention'))` for Django < 2.0

## Usage

* Include webmention information by either:
    * Installing the middleware in `settings.py` (affects all views)
        * Use `webmention.middleware.webmention_middleware` in `MIDDLEWARE` for Django >= 1.10
        * Use `webmention.middleware.WebMentionMiddleware` in `MIDDLEWARE_CLASSES` for older projects
    * Decorating a specific view with `webmention.middleware.include_webmention_information`
* View webmention responses in the Django admin interface and mark them as reviewed as needed

## Development

### Setup

* Install [tox](https://tox.readthedocs.io)

### Running Tests

You can run tests using `tox`:

```shell
$ tox --parallel=auto
```
