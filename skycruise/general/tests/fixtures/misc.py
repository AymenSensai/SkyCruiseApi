import pytest
from django.test import override_settings


@pytest.fixture(autouse=True)
def test_settings():
    with override_settings(SECRET_KEY='django-insecure-#u$pk4&c&f11+v*h=_km$gz$&18*aw2)&f!87a-pc&(s20+vfs'):
        yield
