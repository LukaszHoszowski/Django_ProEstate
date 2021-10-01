from profile import Profile

from django.contrib.auth.models import User


def test_should_create_user_a_profile(user_A: User, app_user_profile_factory: Profile) -> None:
    app_user_profile_factory(user_A, '793454606')
    assert user_A.profile.phone_number == '793454606'


def test_should_update_user_a_profile(user_A: User, user_A_profile: Profile) -> None:
    user_A_profile.phone_number = '999888777'
    assert user_A.profile.phone_number == '999888777'
