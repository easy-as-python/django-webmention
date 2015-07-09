from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns(
    '',
    url(settings.ADMIN_URL, include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
