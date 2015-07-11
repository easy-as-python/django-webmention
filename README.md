# django-webmention

A pluggable implementation of webmention for Django projects.

`$ pip install django-webmention`

* Add `webmention` to `INSTALLED_APPS`
* Add `(r'^webmention', include('webmention.urls'), namespace='webmention')` to top-level `urls.py`
* Include webmention information by either:
    * Adding `webmention.middleware.WebMentionMiddleware` to `MIDDLEWARE_CLASSES` (affects all views)
    * Decorating a specific view with `webmention.middleware.include_webmention_information`
