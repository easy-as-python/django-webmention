from unittest.mock import patch

from django.test import TestCase

from webmention.models import WebMentionResponse


class WebMentionResponseTestCase(TestCase):
    def setUp(self):
        self.source = 'http://example.com'
        self.target = 'http://mysite.com'
        self.response_body = 'foo'

    def test_str(self):
        webmention = WebMentionResponse.objects.create(source=self.source, response_to=self.target, response_body=self.response_body)
        webmention.save()

        self.assertEqual(webmention.source, str(webmention))

    def test_source_for_admin(self):
        webmention = WebMentionResponse.objects.create(source=self.source, response_to=self.target, response_body=self.response_body)
        webmention.save()

        self.assertEqual('<a href="{href}">{href}</a>'.format(href=webmention.source), webmention.source_for_admin())

    def test_response_to_for_admin(self):
        webmention = WebMentionResponse.objects.create(source=self.source, response_to=self.target, response_body=self.response_body)
        webmention.save()

        self.assertEqual('<a href="{href}">{href}</a>'.format(href=webmention.response_to), webmention.response_to_for_admin())

    @patch('webmention.models.WebMentionResponse.save')
    def test_invalidate_when_not_previously_saved(self, mock_save):
        webmention = WebMentionResponse()
        webmention.invalidate()

        self.assertFalse(mock_save.called)

    def test_invalidate_when_previously_saved(self):
        webmention = WebMentionResponse.objects.create(source=self.source, response_to=self.target, response_body=self.response_body)
        webmention.save()
        webmention.invalidate()

        self.assertFalse(webmention.current)

    @patch('webmention.models.WebMentionResponse.save')
    def test_update_when_previously_invalid(self, mock_save):
        webmention = WebMentionResponse.objects.create(source='foo', response_to='bar', response_body='baz', current=False)
        self.assertEqual(1, mock_save.call_count)
        webmention.update(self.source, self.target, self.response_body)

        self.assertTrue(webmention.current)
        self.assertEqual(self.source, webmention.source)
        self.assertEqual(self.target, webmention.response_to)
        self.assertEqual(self.response_body, webmention.response_body)
        self.assertEqual(2, mock_save.call_count)
