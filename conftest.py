import uuid

import pytest
from pytest_factoryboy import register
from selenium import webdriver

from User.tests.factories import UserFactory

register(UserFactory)


# @pytest.fixture(scope='function')
# def func():
#     print("before testcase")
#     yield 10
#     print("after testcase")
#
#
# @pytest.fixture(scope='function')
# def test_password():
#     return 'Testpass123'


@pytest.fixture(scope='function')
def create_user(db, django_user_model, test_password):
    def make_user(**kwargs):
        kwargs['password'] = test_password

        if 'username' not in kwargs:
            kwargs['username'] = str(uuid.uuid4())

        return django_user_model.objects.create_user(**kwargs)

    return make_user


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
