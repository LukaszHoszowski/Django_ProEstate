import tempfile
import uuid
from io import BytesIO
from unittest import mock

import pytest
from PIL import Image

from django.contrib.auth.models import User
from django.core.files import File
from django.core.files.images import ImageFile
from django.core.files.temp import NamedTemporaryFile
from django.core.files.uploadedfile import SimpleUploadedFile
from pytest_factoryboy import register
from selenium import webdriver

from Building.models import Building, PaymentPeriod, Cartography, HousingCooperative
from User.models import Profile
from User.tests.factories import UserFactory

register(UserFactory)


# @pytest.fixture(scope='function')
# def func():
#     print("before testcase")
#     yield 10
#     print("after testcase")


@pytest.fixture(scope='function')
def test_password():
    return 'Testpass123'


@pytest.fixture(scope='function')
def app_user_factory(db):
    def create_app_user(
            username: str,
            password: str,
            first_name: str = "first name",
            last_name: str = "last name",
            email: str = "foo@bar.com",
            is_staff: str = False,
            is_superuser: str = False,
            is_active: str = True,
    ) -> User:
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
        )
        return user

    return create_app_user


@pytest.fixture(scope='function')
def app_user_profile_factory(db):
    def create_app_user_profile(
            user: User,
            phone_number: str,
    ) -> Profile:
        profile = Profile.objects.create(
            user=user,
            phone_number=phone_number,
        )
        return profile

    return create_app_user_profile


@pytest.fixture(scope='function')
def user_A(db, app_user_factory) -> User:
    return app_user_factory("Kermit", "Secret")


@pytest.fixture(scope='function')
def user_B(db, app_user_factory) -> User:
    return app_user_factory("Bob1980", "Testpass123")


@pytest.fixture(scope='function')
def user_A_profile(db, user_A, app_user_profile_factory) -> Profile:
    return app_user_profile_factory(user_A, '793454606')


@pytest.fixture(scope='function')
def create_user(db, django_user_model, test_password):
    def make_user(**kwargs):
        kwargs['password'] = test_password

        if 'username' not in kwargs:
            kwargs['username'] = str(uuid.uuid4())

        return django_user_model.objects.create_user(**kwargs)

    return make_user


def get_image(name='test.png', ext='png', size=(50, 50), color=(256, 0, 0)):
    file_obj = BytesIO()
    image = Image.new("RGBA", size=size, color=color)
    image.save(file_obj, ext)
    file_obj.seek(0)
    return File(file_obj, name=name)


@pytest.fixture(scope='function')
def payment_period_helper(db):
    for x in range(12):
        PaymentPeriod.objects.create(month=x + 1, year=1)


@pytest.fixture(scope='function')
def app_building_factory(db):
    def create_building(
            no_of_flats: int,
            street: str = 'Jesionowa',
            number: str = '10',
            city: str = 'Wrocław',
            zip_code: str = "50-518",
            slug: str = 'jesionowa-10',
            picture=get_image()
    ) -> Building:
        building = Building.objects.create(
            street=street,
            number=number,
            city=city,
            zip_code=zip_code,
            no_of_flats=no_of_flats,
            slug=slug,
            picture=picture
        )
        return building

    return create_building


@pytest.fixture(scope='function')
def app_cartography_factory(db):
    def create_cartography(
            building: Building,
            parcel_identification_number: str = '026401_1.0022.AR_28.86',
            parcel_precinct: int = 1,
            parcel_number: str = '86'
    ) -> Cartography:
        carto = Cartography.objects.create(
            building=building,
            parcel_identification_number=parcel_identification_number,
            parcel_precinct=parcel_precinct,
            parcel_number=parcel_number
        )
        return carto

    return create_cartography


@pytest.fixture(scope='function')
def app_coop_factory(db):
    def create_housing_cooperative(
            name: str = 'Zarządca',
            street: str = 'Jesionowa',
            number: str = '86',
            city: str = 'Wrocław',
            zip_code: str = '50-518',
            email: str = 'op@op.pl',
            phone: str = '793454606',
            logo=get_image()
    ) -> HousingCooperative:
        coop = HousingCooperative.objects.create(
            name=name,
            street=street,
            number=number,
            city=city,
            zip_code=zip_code,
            email=email,
            phone=phone,
            logo=logo
        )
        return coop

    return create_housing_cooperative()


# Selenium
@pytest.fixture(params=['chrome', 'chrome1920'], scope='class')
def driver_init(request):
    if request.param == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        web_driver = webdriver.Chrome(executable_path=r'./test_helpers/chromedriver', options=options)
        request.cls.browser = 'chrome_default'
    elif request.param == 'chrome1920':
        options = webdriver.ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--headless')
        web_driver = webdriver.Chrome(executable_path=r'./test_helpers/chromedriver', options=options)
        request.cls.browser = 'chrome1920x1080'
    else:
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        web_driver = webdriver.Firefox(executable_path=r'./test_helpers/geckodriver', options=options)

    request.cls.driver = web_driver

    yield

    web_driver.close()
