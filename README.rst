django-webmention
=================

A pluggable implementation of webmention for Django projects.

``$ pip install django-webmention``

Add ``webmention`` to ``INSTALLED_APPS`` in your project's
``settings.py``

Add
``(r'^webmention', include('webmention.urls'), namespace='webmention')``
to your project's top-level ``urls.py``
