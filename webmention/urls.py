from django.conf.urls import url

from . import views


app_name = 'webmention'


urlpatterns = [
    url(r'^receive$', views.receive, name='receive'),
]
