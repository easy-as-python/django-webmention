from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import HttpResponseBadRequest, HttpResponseServerError, HttpResponse

from .models import WebMentionResponse
from .resolution import url_resolves, fetch_and_validate_source, SourceFetchError, TargetNotFoundError


@csrf_exempt
@require_POST
def receive(request):
    if 'source' in request.POST and 'target' in request.POST:
        source = request.POST.get('source')
        target = request.POST.get('target')

        if not url_resolves(target):
            return HttpResponseBadRequest('Target URL did not resolve to a resource on the server')

        try:
            webmention = WebMentionResponse()
            webmention.response_body = fetch_and_validate_source(source, target)
            webmention.source = source
            webmention.response_to = target
            webmention.save()
            return HttpResponse('webmention successful')
        except SourceFetchError:
            return HttpResponseBadRequest('Could not fetch source URL')
        except TargetNotFoundError:
            return HttpResponseBadRequest('Source URL did not contain target URL') 
        except Exception as e:
            return HttpResponseServerError(str(e))
    else:
        return HttpResponseBadRequest('webmention source and/or target not in request')

