from urllib.parse import urlparse

import requests

try:
    from django.core.urlresolvers import Resolver404, resolve
except ImportError:
    from django.urls import Resolver404, resolve


def url_resolves(url):
    try:
        resolve(urlparse(url).path)
    except Resolver404:
        return False
    return True


def fetch_and_validate_source(source, target):
    # TODO: Create a sensible default timeout for this request, and make it configurable
    response = requests.get(source)  # noqa: S113 until we have a sensible default timeout
    if response.status_code == 200:
        if target in response.text:
            return response.text
        else:
            raise TargetNotFoundError("Source URL did not contain target URL")
    else:
        raise SourceFetchError("Could not fetch source URL")


class SourceFetchError(Exception):
    pass


class TargetNotFoundError(Exception):
    pass
