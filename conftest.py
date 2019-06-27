import pytest


@pytest.fixture
def test_source():
    return 'http://example.com'


@pytest.fixture
def test_target():
    return 'http://mysite.com'
