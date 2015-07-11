from django.core.urlresolvers import reverse
from django.utils.decorators import decorator_from_middleware


class WebMentionMiddleware(object):
    def process_response(self, request, response):
        response['Link'] = '<{scheme}://{host}{path}>; rel="webmention"'.format(
            scheme=request.scheme,
            host=request.META.get('HTTP_HOST'),
            path=reverse('webmention:receive')
        )
        return response

include_webmention_information = decorator_from_middleware(WebMentionMiddleware)
