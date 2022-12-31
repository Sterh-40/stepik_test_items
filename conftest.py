import time
import pytest
from selenium import webdriver

url_es = "http://selenium1py.pythonanywhere.com/es/catalogue/coders-at-work_207/"
url_fr = "http://selenium1py.pythonanywhere.com/fr/catalogue/coders-at-work_207/"


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='None', help="Choose language: english or russian")


@pytest.fixture(scope="function")
def driver(request):
    language = request.config.getoption('--language')
    print("\nStart browser test..")
    driver = webdriver.Chrome()
    if language == "es":
        driver.get(url_es)
    elif language == "fr":
        driver.get(url_fr)
    else:
        raise pytest.UsageError("-- language should be english or russian")
    yield driver
    print("\nQuit browser..")
    time.sleep(30)
    driver.quit()
