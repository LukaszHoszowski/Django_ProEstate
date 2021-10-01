import pytest
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_user_create():
    User.objects.create_user('test', 'test@test.com', 'test')
    count = User.objects.all().count()
    assert count == 1


def test_should_check_password(db, user_A: User) -> None:
    user_A.set_password("secret")
    assert user_A.check_password("secret") is True


def test_should_not_check_unusable_password(db, user_A: User) -> None:
    user_A.set_password("secret")
    user_A.set_unusable_password()
    assert user_A.check_password("secret") is False


def test_should_create_two_users(user_A: User, user_B: User) -> None:
    assert user_A.pk != user_B.pk


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
