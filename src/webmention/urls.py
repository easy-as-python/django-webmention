from django.urls import re_path

from . import views


app_name = "webmention"


urlpatterns = [re_path(r"^receive$", views.receive, name="receive")]
