import requests

from urllib.parse import urlparse
from django.core.urlresolvers import resolve, Resolver404


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
            raise TargetNotFoundError('Source URL did not contain target URL')
    else:
        raise SourceFetchError('Could not fetch source URL')


class SourceFetchError(Exception):
    pass


class TargetNotFoundError(Exception):
    pass
