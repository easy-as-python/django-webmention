from unittest.mock import Mock
from django.core.urlresolvers import reverse

from django.http import HttpResponse
from django.test import TestCase, Client

from ..middleware import WebMentionMiddleware


class WebMentionMiddlewareTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.middleware = WebMentionMiddleware()

    def test_process_request_creates_link_header(self):
        request = Mock()
        request.scheme = 'http'
        request.META = {'HTTP_HOST': 'example.com'}

        response = HttpResponse()
        response = self.middleware.process_response(request, response)

        expected_link_header = '<{scheme}://{host}{path}>; rel="webmention"'.format(
            scheme=request.scheme,
            host=request.META.get('HTTP_HOST'),
            path=reverse('webmention:receive')
        )

        self.assertIn('Link', response)
        self.assertEqual(expected_link_header, response['Link'])

    def test_process_request_appends_link_header(self):
        request = Mock()
        request.scheme = 'http'
        request.META = {'HTTP_HOST': 'example.com'}

        response = HttpResponse()
        original_link_header = '<meta.rdf>; rel="meta"'
        response['Link'] = original_link_header
        response = self.middleware.process_response(request, response)

        new_link_header = '<{scheme}://{host}{path}>; rel="webmention"'.format(
            scheme=request.scheme,
            host=request.META.get('HTTP_HOST'),
            path=reverse('webmention:receive')
        )

        expected_link_header = ', '.join((original_link_header, new_link_header))

        self.assertIn('Link', response)
        self.assertEqual(expected_link_header, response['Link'])
