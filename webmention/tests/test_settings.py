SECRET_KEY = 'key-for-testing'
INSTALLED_APPS = [
    'webmention',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'tests.sqlite3',
    }
}

ROOT_URLCONF = 'webmention.tests.test_urls'
