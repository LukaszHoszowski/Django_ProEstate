from django.urls import reverse

from User.models import Profile


def test_view_profile(create_user, test_password, client):
    user = create_user(username='Hultaj1980')

    client.login(username=user.username, password=test_password)
    profile = Profile.objects.create(user=user, phone_number='793454606')

    url = reverse('User:profile')

    response = client.get(url)

    assert response.status_code == 200
    assert user.username in response.content.decode('UTF-8')
