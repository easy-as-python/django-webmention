from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^receive$', views.receive, name='receive'),
]
