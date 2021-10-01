from django.urls import reverse


def test_view_main(client):
    url = reverse('main')
    response = client.get(url)

    assert response.status_code == 200
    assert 'stolica' in response.content.decode('UTF-8')


def test_view_about(client):
    url = reverse('about')
    response = client.get(url)

    assert response.status_code == 200
    assert 'Cel projektu' in response.content.decode('UTF-8')


def test_view_404(client):
    url = '404/'
    response = client.get(url)

    assert response.status_code == 404
    assert '404' in response.content.decode('UTF-8')
