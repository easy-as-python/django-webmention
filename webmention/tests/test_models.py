from django.test import TestCase

from ..models import WebMentionResponse


class WebMentionResponseTestCase(TestCase):
    def test_str(self):
        webmention = WebMentionResponse()
        webmention.source = 'http://example.com'
        webmention.response_to = 'http://mysite.com'
        webmention.response_body = 'foo'
        webmention.save()

        self.assertEqual(webmention.source, str(webmention))

    def test_source_for_admin(self):
        webmention = WebMentionResponse()
        webmention.source = 'http://example.com'
        webmention.response_to = 'http://mysite.com'
        webmention.response_body = 'foo'
        webmention.save()

        self.assertEqual('<a href="{href}">{href}</a>'.format(href=webmention.source), webmention.source_for_admin())

    def test_response_to_for_admin(self):
        webmention = WebMentionResponse()
        webmention.source = 'http://example.com'
        webmention.response_to = 'http://mysite.com'
        webmention.response_body = 'foo'
        webmention.save()

        self.assertEqual('<a href="{href}">{href}</a>'.format(href=webmention.response_to), webmention.response_to_for_admin())
