from django.urls import reverse


def test_view_profile(client):
    url = reverse('main')
    response = client.get(url)

    assert response.status_code == 200
    assert 'stolica' in response.content.decode('UTF-8')
