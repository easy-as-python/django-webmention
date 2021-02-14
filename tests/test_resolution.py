from unittest.mock import Mock, patch

import pytest

try:
    from django.core.urlresolvers import Resolver404
except ImportError:
    from django.urls import Resolver404

from webmention.resolution import url_resolves, fetch_and_validate_source, SourceFetchError, TargetNotFoundError


@patch("webmention.resolution.resolve")
def test_url_resolves_when_resolves(mock_resolve, test_source, test_target):
    mock_resolve.return_value = "foo"
    assert url_resolves(test_target)


@patch("webmention.resolution.resolve")
def test_url_resolves_when_does_not_resolve(mock_resolve):
    mock_resolve.side_effect = Resolver404
    assert not url_resolves("http://example.com/page")


@patch("requests.get")
def test_fetch_and_validate_source_happy_path(mock_get, test_source, test_target):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = '<a href="{href}">{href}</a>'.format(href=test_target)
    mock_get.return_value = mock_response

    assert fetch_and_validate_source(test_source, test_target) == mock_response.text


@patch("requests.get")
def test_fetch_and_validate_source_when_source_unavailable(mock_get, test_source, test_target):
    mock_response = Mock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    with pytest.raises(SourceFetchError):
        fetch_and_validate_source(test_source, test_target)


@patch("requests.get")
def test_fetch_and_validate_source_when_source_does_not_contain_target(mock_get, test_source, test_target):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = "foo"
    mock_get.return_value = mock_response

    with pytest.raises(TargetNotFoundError):
        fetch_and_validate_source(test_source, test_target)
