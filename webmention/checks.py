import django
from django.conf import settings
from django.core.checks import Error, register, Tags


@register(Tags.compatibility)
def new_style_middleware_check(app_configs, **kwargs):
    errors = []

    if django.VERSION[1] >= 10 or django.VERSION[0] > 1:
        installed_middlewares = getattr(settings, 'MIDDLEWARE', []) or []
        if 'webmention.middleware.WebMentionMiddleware' in installed_middlewares:
            errors.append(
                Error(
                    'You are attempting to use an old-style middleware class in the MIDDLEWARE setting',
                    hint='Either use MIDDLEWARE_CLASSES or use webmention.middleware.webmention_middleware instead',
                    id='webmention.E001',
                )
            )
    return errors
