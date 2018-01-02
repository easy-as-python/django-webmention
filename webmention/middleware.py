from django.utils.decorators import decorator_from_middleware

try:
    from django.core.urlresolvers import reverse
except ImportError:
    from django.urls import reverse


def add_webmention_headers_to_response(request, response):
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


class WebMentionMiddleware(object):
    def process_response(self, request, response):
        return add_webmention_headers_to_response(request, response)


def webmention_middleware(get_response):
    def middleware(request):
        response = get_response(request)
        return add_webmention_headers_to_response(request, response)

    return middleware


include_webmention_information = decorator_from_middleware(WebMentionMiddleware)
