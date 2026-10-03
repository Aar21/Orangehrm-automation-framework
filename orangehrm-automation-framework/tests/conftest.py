import pytest
from drivers.driver_factory import get_driver
from config.settings import base_url


@pytest.fixture(autouse=True,scope='function')
def setup_teardown(request):
    driver = get_driver("chrome")
    driver.get(base_url)
    request.cls.driver = driver
    yield
    driver.quit()