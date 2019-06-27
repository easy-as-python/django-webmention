from unittest.mock import Mock, patch

import pytest

from django.http import HttpResponseBadRequest, HttpResponse, HttpResponseServerError

from webmention.views import receive
from webmention.resolution import SourceFetchError, TargetNotFoundError


def test_receive_when_source_not_in_post_data(test_target):
    request = Mock()
    request.method = 'POST'
    request.POST = {'target': test_target}

    response = receive(request)

    assert isinstance(response, HttpResponseBadRequest)

def test_receive_when_target_not_in_post_data(test_source):
    request = Mock()
    request.method = 'POST'
    request.POST = {'source': test_source}

    response = receive(request)

    assert isinstance(response, HttpResponseBadRequest)

@patch('webmention.views.url_resolves')
def test_receive_when_target_does_not_resolve(mock_url_resolves, test_source, test_target):
    request = Mock()
    request.method = 'POST'
    request.POST = {'source': test_source, 'target': test_target}

    mock_url_resolves.return_value = False
    response = receive(request)

    mock_url_resolves.assert_called_once_with(test_target)
    assert isinstance(response, HttpResponseBadRequest)

@pytest.mark.django_db
@patch('webmention.views.WebMentionResponse.update')
@patch('webmention.views.fetch_and_validate_source')
@patch('webmention.views.url_resolves')
def test_receive_happy_path(mock_url_resolves, mock_fetch_and_validate_source, mock_update, test_source, test_target):
    request = Mock()
    request.method = 'POST'
    request.POST = {'source': test_source, 'target': test_target}

    mock_url_resolves.return_value = True
    mock_fetch_and_validate_source.return_value = 'foo'
    response = receive(request)

    mock_fetch_and_validate_source.assert_called_once_with(test_source, test_target)
    mock_update.assert_called_once_with(test_source, test_target, mock_fetch_and_validate_source.return_value)
    mock_url_resolves.assert_called_once_with(test_target)
    assert isinstance(response, HttpResponse)

@pytest.mark.django_db
@patch('webmention.views.WebMentionResponse.invalidate')
@patch('webmention.views.fetch_and_validate_source')
@patch('webmention.views.url_resolves')
def test_receive_when_source_unavailable(mock_url_resolves, mock_fetch_and_validate_source, mock_invalidate, test_source, test_target):
    request = Mock()
    request.method = 'POST'
    request.POST = {'source': test_source, 'target': test_target}

    mock_url_resolves.return_value = True
    mock_fetch_and_validate_source.side_effect = SourceFetchError
    response = receive(request)

    mock_fetch_and_validate_source.assert_called_once_with(test_source, test_target)
    mock_url_resolves.assert_called_once_with(test_target)
    assert mock_invalidate.call_count == 1
    assert isinstance(response, HttpResponseBadRequest)

@pytest.mark.django_db
@patch('webmention.views.WebMentionResponse.invalidate')
@patch('webmention.views.fetch_and_validate_source')
@patch('webmention.views.url_resolves')
def test_receive_when_source_does_not_contain_target(mock_url_resolves, mock_fetch_and_validate_source, mock_invalidate, test_source, test_target):
    request = Mock()
    request.method = 'POST'
    request.POST = {'source': test_source, 'target': test_target}

    mock_url_resolves.return_value = True
    mock_fetch_and_validate_source.side_effect = TargetNotFoundError
    response = receive(request)

    mock_fetch_and_validate_source.assert_called_once_with(test_source, test_target)
    mock_url_resolves.assert_called_once_with(test_target)
    assert mock_invalidate.call_count == 1
    assert isinstance(response, HttpResponseBadRequest)

@pytest.mark.django_db
@patch('webmention.views.fetch_and_validate_source')
@patch('webmention.views.url_resolves')
def test_receive_when_general_exception_occurs(mock_url_resolves, mock_fetch_and_validate_source, test_source, test_target):
    request = Mock()
    request.method = 'POST'
    request.POST = {'source': test_source, 'target': test_target}

    mock_url_resolves.return_value = True
    mock_fetch_and_validate_source.side_effect = Exception
    response = receive(request)

    mock_fetch_and_validate_source.assert_called_once_with(test_source, test_target)
    mock_url_resolves.assert_called_once_with(test_target)
    assert isinstance(response, HttpResponseServerError)
