from django.urls import reverse


def test_view_profile(create_user, test_password, client):
    user = create_user(username='Hultaj1980')
    url = reverse('profile')

    client.login(username=user.username, password=test_password)
    response = client.get(url)

    assert response.status_code == 200
    assert user.username in response.content.decode('UTF-8')
