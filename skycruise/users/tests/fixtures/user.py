import pytest
from model_bakery import baker


@pytest.fixture
def user(db):
    user = baker.make('users.User', username='user', email='user@example.com')
    user.set_password('pass1234')
    user.save()
    return user


@pytest.fixture
def ia_user(db):
    return baker.make('users.User', username='ia')
