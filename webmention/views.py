import requests
from urllib.parse import urlparse

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core.urlresolvers import resolve, Resolver404
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError

def url_resolves(url):
    try:
        resolve(urlparse(url).path)
    except Resolver404:
        return False
    return True

def fetch_and_validate_source(source, target):
    response = requests.get(source)
    if response.status_code == 200:
        if target in str(response.content):
            return response.content
        else:
            raise TargetNotFoundError
    else:
        raise SourceFetchError

@csrf_exempt
@require_POST
def receive(request):
    if 'source' in request.POST and 'target' in request.POST:
        source = request.POST.get('source')
        target = request.POST.get('target')

        if not url_resolves(target):
            return HttpResponseBadRequest('Target URL did not resolve to a resource on the server')

        try:
            return HttpResponse(fetch_and_validate_source(source, target))
        except SourceFetchError:
            return HttpResponseBadRequest('Could not fetch source URL')
        except TargetNotFoundError:
            return HttpResponseBadRequest('Source URL did not contain target URL') 
        except Exception as e:
            return HttpResponseServerError(str(e))
    else:
        return HttpResponseBadRequest('webmention source and/or target not in request')

class SourceFetchError(Exception):
    pass

class TargetNotFoundError(Exception):
    pass
