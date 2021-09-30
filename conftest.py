import pytest
from pytest_factoryboy import register

from User.tests.factories import UserFactory

register(UserFactory)


@pytest.fixture(scope='function')
def func():
    print("before testcase")
    yield 10
    print("after testcase")


@pytest.fixture(scope='function')
def test_password():
    return 'Testpass123'


@pytest.fixture(scope='function')
def create_user(db, django_user_model, test_password):
    def make_user(**kwargs):
        

