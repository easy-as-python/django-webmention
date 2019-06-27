from unittest.mock import patch

import pytest

from webmention.models import WebMentionResponse


@pytest.fixture
def test_response_body():
    return 'foo'


@pytest.mark.django_db
def test_str(test_source, test_target, test_response_body):
    webmention = WebMentionResponse.objects.create(source=test_source, response_to=test_target, response_body=test_response_body)
    webmention.save()

    assert str(webmention) == webmention.source

@pytest.mark.django_db
def test_source_for_admin(test_source, test_target, test_response_body):
    webmention = WebMentionResponse.objects.create(source=test_source, response_to=test_target, response_body=test_response_body)
    webmention.save()

    assert webmention.source_for_admin() == '<a href="{href}">{href}</a>'.format(href=webmention.source)

@pytest.mark.django_db
def test_response_to_for_admin(test_source, test_target, test_response_body):
    webmention = WebMentionResponse.objects.create(source=test_source, response_to=test_target, response_body=test_response_body)
    webmention.save()

    assert webmention.response_to_for_admin() == '<a href="{href}">{href}</a>'.format(href=webmention.response_to)

@patch('webmention.models.WebMentionResponse.save')
def test_invalidate_when_not_previously_saved(mock_save):
    webmention = WebMentionResponse()
    webmention.invalidate()

    assert not mock_save.called

@pytest.mark.django_db
def test_invalidate_when_previously_saved(test_source, test_target, test_response_body):
    webmention = WebMentionResponse.objects.create(source=test_source, response_to=test_target, response_body=test_response_body)
    webmention.save()
    webmention.invalidate()

    assert not webmention.current

@patch('webmention.models.WebMentionResponse.save')
def test_update_when_previously_invalid(mock_save, test_source, test_target, test_response_body):
    webmention = WebMentionResponse.objects.create(source='foo', response_to='bar', response_body='baz', current=False)
    assert mock_save.call_count == 1
    webmention.update(test_source, test_target, test_response_body)

    assert webmention.current
    assert webmention.source == test_source
    assert webmention.response_to == test_target
    assert webmention.response_body == test_response_body
    assert mock_save.call_count == 2
