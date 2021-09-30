import pytest
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_user_create():
    User.objects.create_user('test', 'test@test.com', 'test')
    count = User.objects.all().count()
    assert count == 1


@pytest.mark.django_db
def test_check_set_user_password():
    user = User.objects.create_user('test')
    user.set_password('new_password')
    assert user.check_password('new_password') is True


@pytest.mark.parametrize(
    'first_name, last_name',
    [
        ('John', 'Smith'),
        ('John1', 'Smith3'),
    ]
)
def test_user_create_instance(db, user_factory, first_name, last_name):
    user = user_factory(
        first_name=first_name,
        last_name=last_name,
    )

    count = User.objects.all().count()
    assert count == 1
