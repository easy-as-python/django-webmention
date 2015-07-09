from django.core.urlresolvers import reverse


class WebMentionMiddleware(object):
    def process_response(self, request, response):
        response['Link'] = '<{scheme}://{host}{path}>; rel="webmention"'.format(scheme=request.scheme, host=request.META.get('HTTP_HOST'), path=reverse('webmention:receive'))
        return response
