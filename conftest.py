import uuid

import pytest
from django.contrib.auth.models import User
from pytest_factoryboy import register
from selenium import webdriver

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


@pytest.fixture
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


@pytest.fixture(scope='function')
def app_building_factory(db):
    def create_building(
            street: str = 'Jesionowa',
            number: str = '10',
            city: str = 'Wrocław',
            zip_code: str = "50-518",
            no_of_flats: int = 10,
            picture = False,
    ) -> User:
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            pictire=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
        )
        return user

    return create_app_user


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
