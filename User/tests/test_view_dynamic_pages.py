from django.urls import reverse


def test_view_signup_view(client):
    url = reverse('User:signup')
    response = client.get(url)

    assert response.status_code == 200
    assert 'Zarejestruj' in response.content.decode('UTF-8')


def test_view_profile_creation_user_logged(user_A, client):
    client.force_login(user_A)
    url = reverse('User:profile_create_additional')
    response = client.get(url)

    assert response.status_code == 200
    assert 'Zapisz' in response.content.decode('UTF-8')


def test_view_profile_creation_user_anonymous(client):
    url = reverse('User:profile_create_additional')
    response = client.get(url)

    assert response.status_code == 302
    assert 'login' in response.url


def test_view_profile_creation_flat_user_logged(user_A, client):
    client.force_login(user_A)
    url = reverse('User:profile_create_flat')
    response = client.get(url)

    assert response.status_code == 200
    assert 'Dodaj' in response.content.decode('UTF-8')


def test_view_profile_creation_flat_user_anonymous(client):
    url = reverse('User:profile_create_flat')
    response = client.get(url)

    assert response.status_code == 302
    assert 'login' in response.url


def test_view_profile_user_logged(user_A, user_A_profile, client):
    client.force_login(user_A)
    user_A_profile.user = user_A
    url = reverse('User:profile')
    response = client.get(url)

    assert response.status_code == 200
    assert user_A.username in response.content.decode('UTF-8')


def test_view_profile_user_anonymous(client):
    url = reverse('User:profile')
    response = client.get(url)

    assert response.status_code == 302
    assert 'login' in response.url


def test_view_profile_update_user_logged(user_A, user_A_profile, client):
    client.force_login(user_A)
    user_A_profile.user = user_A
    url = reverse('User:profile_update')
    response = client.get(url)

    assert response.status_code == 200
    assert user_A.profile.phone_number in response.content.decode('UTF-8')


def test_view_profile_update_user_anonymous(client):
    url = reverse('User:profile_update')
    response = client.get(url)

    assert response.status_code == 302
    assert 'login' in response.url


def test_view_profile_pass_change_user_logged(user_A, user_A_profile, client):
    client.force_login(user_A)
    user_A_profile.user = user_A
    url = reverse('User:pass_change')
    response = client.get(url)

    assert response.status_code == 200
    assert 'Stare hasło' in response.content.decode('UTF-8')


def test_view_profile_pass_change_user_anonymous(client):
    url = reverse('User:pass_change')
    response = client.get(url)

    assert response.status_code == 302
    assert 'login' in response.url


def test_view_profile_delete_user_logged(user_A, user_A_profile, client):
    client.force_login(user_A)
    user_A_profile.user = user_A
    url = reverse('User:delete_user')
    response = client.get(url)

    assert response.status_code == 200
    assert 'Potwierdź' in response.content.decode('UTF-8')


def test_view_profile_delete_user_anonymous(client):
    url = reverse('User:delete_user')
    response = client.get(url)

    assert response.status_code == 302
    assert 'login' in response.url


def test_view_profile_logout(user_A, user_A_profile, client):
    client.login(username="Kermit", password="Secret")
    user_A_profile.user = user_A

    url = reverse('User:user_logout')
    response = client.get(url)

    assert response.status_code == 302
    assert response['Location'] == reverse('main')


def test_view_profile_login(client):
    url = reverse('User:user_login')
    response = client.get(url)

    assert response.status_code == 200
    assert 'Zaloguj się' in response.content.decode('UTF-8')


def test_view_report_failure_user_logged(user_A, user_A_profile, client):
    client.force_login(user_A)
    user_A_profile.user = user_A
    url = reverse('User:report_failure')
    response = client.get(url)

    assert response.status_code == 200
    assert 'Wyślij' in response.content.decode('UTF-8')


def test_view_report_failure_user_anonymous(client):
    url = reverse('User:report_failure')
    response = client.get(url)

    assert response.status_code == 302
    assert 'login' in response.url


def test_view_contact_neighbour_user_logged(user_A, user_A_profile, client):
    client.force_login(user_A)
    user_A_profile.user = user_A
    url = reverse('User:contact_neighbour')
    response = client.get(url)

    assert response.status_code == 200
    assert 'Wyślij' in response.content.decode('UTF-8')


def test_view_contact_neighbour_user_anonymous(client):
    url = reverse('User:contact_neighbour')
    response = client.get(url)

    assert response.status_code == 302
    assert 'login' in response.url
