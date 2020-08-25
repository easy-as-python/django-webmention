# django-webmention [![PyPI version](https://badge.fury.io/py/django-webmention.svg)](https://badge.fury.io/py/django-webmention) [![Build Status](https://travis-ci.org/easy-as-python/django-webmention.svg?branch=master)](https://travis-ci.org/easy-as-python/django-webmention)

[webmention](https://www.w3.org/TR/webmention/) for Django projects.

## What this project is

This package provides a way to integrate [webmention endpoint discovery](https://www.w3.org/TR/webmention/#sender-discovers-receiver-webmention-endpoint) and [webmention receipts](https://www.w3.org/TR/webmention/#receiving-webmentions) into your project. Once you follow the installation instructions, you should be able to use something like [webmention.rocks](https://webmention.rocks/) to generate a test webmention and see it in the Django admin panel.

Once you receive a webmention, you can click through to the page the webmention was sent from and see what people are saying about your site. Afterward, you can mark the webmention as reviewed in the Django admin so you can more easily see the latest webmentions you receive.

Once you verify that you're receiving webmentions successfully, you can use the webmention information as you like. As an example, you could query the webmentions that are responses to a specific page and display them on that page.

## What this project isn't

This package does not currently provide functionality for [sending webmentions](https://www.w3.org/TR/webmention/#sending-webmentions).

## Installation

`$ pip install django-webmention`

* Add `'webmention'` to `INSTALLED_APPS`
* Run `python manage.py migrate webmention`
* Add the URL patterns to your top-level `urls.py`
    * `path('webmention/', include('webmention.urls'))` for Django >= 2.0
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
