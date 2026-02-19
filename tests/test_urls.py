from django.urls import include, re_path

urlpatterns = [re_path(r"^webmention", include("webmention.urls", namespace="webmention"))]
