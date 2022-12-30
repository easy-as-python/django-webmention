from unittest.mock import Mock

import pytest

try:
    from django.core.urlresolvers import reverse
except ImportError:
    from django.urls import reverse

from django.http import HttpResponse

from webmention.middleware import WebMentionMiddleware


@pytest.fixture
def middleware():
    return WebMentionMiddleware(get_response=Mock())


def test_process_request_creates_link_header(middleware):
    request = Mock()
    request.scheme = "http"
    request.META = {"HTTP_HOST": "example.com"}

    response = HttpResponse()
    response = middleware.process_response(request, response)

    expected_link_header = '<{scheme}://{host}{path}>; rel="webmention"'.format(
        scheme=request.scheme, host=request.META.get("HTTP_HOST"), path=reverse("webmention:receive")
    )

    assert "Link" in response
    assert response["Link"] == expected_link_header


def test_process_request_appends_link_header(middleware):
    request = Mock()
    request.scheme = "http"
    request.META = {"HTTP_HOST": "example.com"}

    response = HttpResponse()
    original_link_header = '<meta.rdf>; rel="meta"'
    response["Link"] = original_link_header
    response = middleware.process_response(request, response)

    new_link_header = '<{scheme}://{host}{path}>; rel="webmention"'.format(
        scheme=request.scheme, host=request.META.get("HTTP_HOST"), path=reverse("webmention:receive")
    )

    expected_link_header = ", ".join((original_link_header, new_link_header))

    assert "Link" in response
    assert response["Link"] == expected_link_header
