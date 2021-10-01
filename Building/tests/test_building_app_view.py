from django.contrib.auth.models import User
from django.urls import reverse

from Building.models import Building, Cartography, HousingCooperative, Flat


def test_view_buildings_user_logged(user_A: User, app_building_factory: Building, payment_period_helper, client):
    client.force_login(user_A)
    payment_period_helper
    building = app_building_factory(1)

    url = reverse('Building:buildings')
    response = client.get(url)

    assert response.status_code == 200
    assert str(building).upper() in str(response.content.decode('UTF-8'))


def test_view_buildings_user_anonymous(client, app_building_factory: Building, payment_period_helper):
    payment_period_helper
    building = app_building_factory(1)

    url = reverse('Building:buildings')
    response = client.get(url)

    assert response.status_code == 302
    assert 'login' in response.url


def test_view_building_details_user_logged(user_A: User, app_building_factory: Building, payment_period_helper, client):
    client.force_login(user_A)
    payment_period_helper
    building = app_building_factory(1)

    url = reverse('Building:building_details', args=[building.slug])
    response = client.get(url)

    print(response.content.decode('UTF-8'))

    assert response.status_code == 200
    assert building.street in response.content.decode('UTF-8')


def test_view_building_details_user_anonymous(client, app_building_factory: Building, payment_period_helper):
    payment_period_helper
    building = app_building_factory(1)

    url = reverse('Building:building_details', args=[building.slug])
    response = client.get(url)

    assert response.status_code == 302
    assert 'login' in response.url


def test_view_building_flats_user_logged(user_A: User, app_building_factory: Building, payment_period_helper, client):
    client.force_login(user_A)
    payment_period_helper
    building = app_building_factory(1)

    url = reverse('Building:building_flats', args=[building.slug])
    response = client.get(url)

    assert response.status_code == 200
    assert 'Pełna własność' in response.content.decode('UTF-8')


def test_view_building_flats_user_anonymous(client, app_building_factory: Building, payment_period_helper):
    payment_period_helper
    building = app_building_factory(1)

    url = reverse('Building:building_flats', args=[building.slug])
    response = client.get(url)

    assert response.status_code == 302
    assert 'login' in response.url


def test_view_building_cartography_user_logged(user_A: User, app_building_factory: Building,
                                               app_cartography_factory: Cartography, payment_period_helper, client):
    client.force_login(user_A)
    payment_period_helper
    building = app_building_factory(1)

    carto = app_cartography_factory(building)

    url = reverse('Building:building_cartography', args=[building.slug])
    response = client.get(url, slug=building.slug)

    assert response.status_code == 200
    assert '026401_1.0022.AR_28.86' in response.content.decode('UTF-8')


def test_view_building_cartography_user_anonymous(client, app_building_factory: Building,
                                                  app_cartography_factory: Cartography, payment_period_helper):
    payment_period_helper
    building = app_building_factory(1)
    carto = app_cartography_factory(building)

    url = reverse('Building:building_cartography', args=[building.slug])
    response = client.get(url)

    assert response.status_code == 302
    assert 'login' in response.url


def test_view_building_coop_user_logged(user_A: User, app_building_factory: Building,
                                        app_coop_factory: HousingCooperative, payment_period_helper, client):
    client.force_login(user_A)
    payment_period_helper
    building = app_building_factory(1)

    coop = app_coop_factory
    coop.building_set.add(building)

    url = reverse('Building:building_coop', args=[building.slug])
    response = client.get(url)

    assert response.status_code == 200
    assert 'Zarządca' in response.content.decode('UTF-8')


def test_view_building_coop_user_anonymous(client, app_building_factory: Building,
                                           app_coop_factory: HousingCooperative, payment_period_helper):
    payment_period_helper
    building = app_building_factory(1)
    coop = app_coop_factory
    coop.building_set.add(building)

    url = reverse('Building:building_coop', args=[building.slug])
    response = client.get(url)

    assert response.status_code == 302
    assert 'login' in response.url


def test_view_building_photos_user_logged(user_A: User, app_building_factory: Building,
                                          payment_period_helper, client):
    client.force_login(user_A)
    payment_period_helper
    building = app_building_factory(1)

    url = reverse('Building:building_photos', args=[building.slug])
    response = client.get(url)

    assert response.status_code == 200
    assert 'Nie dodano jeszcze zdjęć' in response.content.decode('UTF-8')


def test_view_building_photos_user_anonymous(client, app_building_factory: Building,
                                             payment_period_helper):
    payment_period_helper
    building = app_building_factory(1)

    url = reverse('Building:building_photos', args=[building.slug])
    response = client.get(url)

    assert response.status_code == 302
    assert 'login' in response.url


def test_view_building_add_photos_user_logged(user_A: User, app_building_factory: Building,
                                              payment_period_helper, client):
    client.force_login(user_A)
    payment_period_helper
    building = app_building_factory(1)

    url = reverse('Building:building_photos_add', args=[building.slug])
    response = client.get(url)

    assert response.status_code == 200
    assert 'Zapisz' in response.content.decode('UTF-8')


def test_view_building_add_photos_user_anonymous(client, app_building_factory: Building,
                                                 payment_period_helper):
    payment_period_helper
    building = app_building_factory(1)

    url = reverse('Building:building_photos_add', args=[building.slug])
    response = client.get(url)

    assert response.status_code == 302
    assert 'login' in response.url


def test_view_building_documents_user_logged(user_A: User, app_building_factory: Building,
                                             payment_period_helper, client):
    client.force_login(user_A)
    payment_period_helper
    building = app_building_factory(1)

    url = reverse('Building:building_documents', args=[building.slug])
    response = client.get(url)

    assert response.status_code == 200
    assert 'Nie dodano jeszcze dokumentów' in response.content.decode('UTF-8')


def test_view_building_documents_user_anonymous(client, app_building_factory: Building,
                                                payment_period_helper):
    payment_period_helper
    building = app_building_factory(1)

    url = reverse('Building:building_documents', args=[building.slug])
    response = client.get(url)

    assert response.status_code == 302
    assert 'login' in response.url


def test_view_building_add_documents_user_logged(user_A: User, app_building_factory: Building,
                                                 payment_period_helper, client):
    client.force_login(user_A)
    payment_period_helper
    building = app_building_factory(1)

    url = reverse('Building:building_docs_add', args=[building.slug])
    response = client.get(url)

    assert response.status_code == 200
    assert 'Zapisz' in response.content.decode('UTF-8')


def test_view_building_add_documents_user_anonymous(client, app_building_factory: Building,
                                                    payment_period_helper):
    payment_period_helper
    building = app_building_factory(1)

    url = reverse('Building:building_docs_add', args=[building.slug])
    response = client.get(url)

    assert response.status_code == 302
    assert 'login' in response.url


def test_view_building_flat_details_user_logged(user_A: User, app_building_factory: Building,
                                                payment_period_helper, client):
    client.force_login(user_A)
    payment_period_helper
    building = app_building_factory(1)

    url = reverse('Building:flat_details', args=[building.slug, building.flat_set.all().first().id])
    response = client.get(url)

    assert response.status_code == 200
    assert 'Dopisz się do mieszkania' in response.content.decode('UTF-8')


def test_view_building_flat_details_user_anonymous(client, app_building_factory: Building,
                                                   payment_period_helper):
    payment_period_helper
    building = app_building_factory(1)

    url = reverse('Building:flat_details', args=[building.slug, building.flat_set.all().first().id])
    response = client.get(url)

    assert response.status_code == 302
    assert 'login' in response.url


def test_view_building_flat_update_user_logged(user_A: User, app_building_factory: Building,
                                               payment_period_helper, client):
    client.force_login(user_A)
    payment_period_helper
    building = app_building_factory(1)

    url = reverse('Building:flat_update', args=[building.slug, building.flat_set.all().first().id])
    response = client.get(url)

    assert response.status_code == 200
    assert 'suffix' in response.content.decode('UTF-8')


def test_view_building_flat_update_user_anonymous(client, app_building_factory: Building,
                                                  payment_period_helper):
    payment_period_helper
    building = app_building_factory(1)

    url = reverse('Building:flat_update', args=[building.slug, building.flat_set.all().first().id])
    response = client.get(url)

    assert response.status_code == 302
    assert 'login' in response.url


def test_view_building_user_to_flat_user_logged(user_A: User, app_building_factory: Building,
                                                payment_period_helper, client):
    client.force_login(user_A)
    payment_period_helper
    building = app_building_factory(1)
    flat = building.flat_set.all().first()

    url = reverse('Building:flat_add_user', args=[flat.id])
    response = client.post(url)

    assert response.status_code == 302
    assert user_A.flat_set.all().first() == flat


def test_view_building_user_to_flat_update_user_anonymous(client, app_building_factory: Building,
                                                          payment_period_helper):
    payment_period_helper
    building = app_building_factory(1)

    url = reverse('Building:flat_add_user', args=[building.flat_set.all().first().id])
    response = client.post(url)

    assert response.status_code == 302
    assert 'login' in response.url


def test_view_building_user_from_flat_user_logged(user_A: User, app_building_factory: Building,
                                                payment_period_helper, client):
    client.force_login(user_A)
    payment_period_helper
    building = app_building_factory(1)
    flat = building.flat_set.all().first()

    url = reverse('Building:flat_delete_user', args=[flat.id])
    response = client.post(url)

    assert response.status_code == 302
    assert user_A.flat_set.all().first() != flat


def test_view_building_user_from_flat_update_user_anonymous(client, app_building_factory: Building,
                                                          payment_period_helper):
    payment_period_helper
    building = app_building_factory(1)

    url = reverse('Building:flat_delete_user', args=[building.flat_set.all().first().id])
    response = client.post(url)

    assert response.status_code == 302
    assert 'login' in response.url