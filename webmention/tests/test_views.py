from unittest.mock import Mock, patch

from django.test import TestCase
from django.http import HttpResponseBadRequest, HttpResponse, HttpResponseServerError

from ..views import receive
from ..resolution import SourceFetchError, TargetNotFoundError


class ReceiveTestCase(TestCase):
    def setUp(self):
        self.source = 'http://example.com'
        self.target = 'http://mysite.com'

    def test_receive_when_source_not_in_post_data(self):
        request = Mock()
        request.method = 'POST'
        request.POST = {'target': self.target}

        response = receive(request)

        self.assertTrue(isinstance(response, HttpResponseBadRequest))

    def test_receive_when_target_not_in_post_data(self):
        request = Mock()
        request.method = 'POST'
        request.POST = {'source': self.source}

        response = receive(request)

        self.assertTrue(isinstance(response, HttpResponseBadRequest))

    @patch('webmention.views.url_resolves')
    def test_receive_when_target_does_not_resolve(self, mock_url_resolves):
        request = Mock()
        request.method = 'POST'
        request.POST = {'source': self.source, 'target': self.target}

        mock_url_resolves.return_value = False
        response = receive(request)

        mock_url_resolves.assert_called_once_with(self.target)
        self.assertTrue(isinstance(response, HttpResponseBadRequest))

    @patch('webmention.views.WebMentionResponse.update')
    @patch('webmention.views.fetch_and_validate_source')
    @patch('webmention.views.url_resolves')
    def test_receive_happy_path(self, mock_url_resolves, mock_fetch_and_validate_source, mock_update):
        request = Mock()
        request.method = 'POST'
        request.POST = {'source': self.source, 'target': self.target}

        mock_url_resolves.return_value = True
        mock_fetch_and_validate_source.return_value = 'foo'
        response = receive(request)

        mock_fetch_and_validate_source.assert_called_once_with(self.source, self.target)
        mock_update.assert_called_once_with(self.source, self.target, mock_fetch_and_validate_source.return_value)
        mock_url_resolves.assert_called_once_with(self.target)
        self.assertTrue(isinstance(response, HttpResponse))

    @patch('webmention.views.WebMentionResponse.invalidate')
    @patch('webmention.views.fetch_and_validate_source')
    @patch('webmention.views.url_resolves')
    def test_receive_when_source_unavailable(self, mock_url_resolves, mock_fetch_and_validate_source, mock_invalidate):
        request = Mock()
        request.method = 'POST'
        request.POST = {'source': self.source, 'target': self.target}

        mock_url_resolves.return_value = True
        mock_fetch_and_validate_source.side_effect = SourceFetchError
        response = receive(request)

        mock_fetch_and_validate_source.assert_called_once_with(self.source, self.target)
        mock_url_resolves.assert_called_once_with(self.target)
        self.assertEqual(1, mock_invalidate.call_count)
        self.assertTrue(isinstance(response, HttpResponseBadRequest))

    @patch('webmention.views.WebMentionResponse.invalidate')
    @patch('webmention.views.fetch_and_validate_source')
    @patch('webmention.views.url_resolves')
    def test_receive_when_source_does_not_contain_target(self, mock_url_resolves, mock_fetch_and_validate_source, mock_invalidate):
        request = Mock()
        request.method = 'POST'
        request.POST = {'source': self.source, 'target': self.target}

        mock_url_resolves.return_value = True
        mock_fetch_and_validate_source.side_effect = TargetNotFoundError
        response = receive(request)

        mock_fetch_and_validate_source.assert_called_once_with(self.source, self.target)
        mock_url_resolves.assert_called_once_with(self.target)
        self.assertEqual(1, mock_invalidate.call_count)
        self.assertTrue(isinstance(response, HttpResponseBadRequest))

    @patch('webmention.views.fetch_and_validate_source')
    @patch('webmention.views.url_resolves')
    def test_receive_when_general_exception_occurs(self, mock_url_resolves, mock_fetch_and_validate_source):
        request = Mock()
        request.method = 'POST'
        request.POST = {'source': self.source, 'target': self.target}

        mock_url_resolves.return_value = True
        mock_fetch_and_validate_source.side_effect = Exception
        response = receive(request)

        mock_fetch_and_validate_source.assert_called_once_with(self.source, self.target)
        mock_url_resolves.assert_called_once_with(self.target)
        self.assertTrue(isinstance(response, HttpResponseServerError))
