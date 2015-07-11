from django.core.urlresolvers import reverse
from django.utils.decorators import decorator_from_middleware


class WebMentionMiddleware(object):
    def process_response(self, request, response):
        link_header = '<{scheme}://{host}{path}>; rel="webmention"'.format(
            scheme=request.scheme,
            host=request.META.get('HTTP_HOST'),
            path=reverse('webmention:receive')
        )
        if not response.get('Link'):
            response['Link'] = link_header
        else:
            response['Link'] = ', '.join((response['Link'], link_header))

        return response

include_webmention_information = decorator_from_middleware(WebMentionMiddleware)
