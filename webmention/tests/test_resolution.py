from unittest.mock import Mock, patch
from django.core.urlresolvers import Resolver404

from django.test import TestCase

from ..resolution import url_resolves, fetch_and_validate_source, SourceFetchError, TargetNotFoundError


class ResolutionTestCase(TestCase):
    def setUp(self):
        self.source = 'http://example.com'
        self.target = 'http://mysite.com'

    @patch('webmention.resolution.resolve')
    def test_url_resolves_when_resolves(self, mock_resolve):
        mock_resolve.return_value = 'foo'
        self.assertTrue(url_resolves(self.target))

    @patch('webmention.resolution.resolve')
    def test_url_resolves_when_does_not_resolve(self, mock_resolve):
        mock_resolve.side_effect = Resolver404
        self.assertFalse(url_resolves('http://example.com/page'))

    @patch('requests.get')
    def test_fetch_and_validate_source_happy_path(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = '<a href="{href}">{href}</a>'.format(href=self.target)
        mock_get.return_value = mock_response

        self.assertEqual(mock_response.content, fetch_and_validate_source(self.source, self.target))

    @patch('requests.get')
    def test_fetch_and_validate_source_when_source_unavailable(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        self.assertRaises(SourceFetchError, fetch_and_validate_source, self.source, self.target)

    @patch('requests.get')
    def test_fetch_and_validate_source_when_source_does_not_contain_target(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = 'foo'
        mock_get.return_value = mock_response

        self.assertRaises(TargetNotFoundError, fetch_and_validate_source, self.source, self.target)
