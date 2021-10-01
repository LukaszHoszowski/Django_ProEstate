import os
import time

import pytest


@pytest.mark.usefixtures('driver_init')
class TestUrlChrome:

    def test_open_url(self, live_server):
        self.driver.get(f'{live_server.url}/admin/')

        assert 'Zaloguj się | Administracja stroną Django' in self.driver.title


def take_screenshot(driver, name):
    time.sleep(1)

    os.makedirs(os.path.join('screenshot', os.path.dirname(name)), exist_ok=True)
    driver.save_screenshot(os.path.join('screenshot', name))


@pytest.mark.usefixtures('driver_init')
class Screenshot:

    def screenshot_admin(self, live_server):
        self.driver.get(f'{live_server.url}/admin/')

        take_screenshot(self.driver, f'admin/admin_{self.browser}.png')

        assert 'Zaloguj się | Administracja stroną Django' in self.driver.title
