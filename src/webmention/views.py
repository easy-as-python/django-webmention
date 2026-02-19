from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import WebMentionResponse
from .resolution import SourceFetchError, TargetNotFoundError, fetch_and_validate_source, url_resolves


@csrf_exempt
@require_POST
def receive(request):
    if "source" in request.POST and "target" in request.POST:
        source = request.POST.get("source")
        target = request.POST.get("target")
        webmention = None

        if not url_resolves(target):
            return HttpResponseBadRequest("Target URL did not resolve to a resource on the server")

        try:
            try:
                webmention = WebMentionResponse.objects.get(source=source, response_to=target)
            except WebMentionResponse.DoesNotExist:
                webmention = WebMentionResponse()

            response_body = fetch_and_validate_source(source, target)
            webmention.update(source, target, response_body)
            return HttpResponse("The webmention was successfully received", status=202)
        except (SourceFetchError, TargetNotFoundError) as e:
            if webmention:
                webmention.invalidate()
            return HttpResponseBadRequest(str(e))
        except Exception as e:
            return HttpResponseServerError(str(e))
    else:
        return HttpResponseBadRequest("webmention source and/or target not in request")
