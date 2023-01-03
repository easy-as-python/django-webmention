from django.urls import re_path, include

urlpatterns = [re_path(r"^webmention", include("webmention.urls", namespace="webmention"))]
