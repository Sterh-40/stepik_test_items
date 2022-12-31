import time
import pytest
from selenium import webdriver

url_eng = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
url_rus = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"


def pytest_addoption(parser):
    parser.addoption('--lang_type', action='store', default='None', help="Choose language: english or russian")


@pytest.fixture(scope="function")
def driver(request):
    lang_type = request.config.getoption('--lang_type')
    print("\nStart browser test..")
    driver = webdriver.Chrome()
    if lang_type == "english":
        driver.get(url_eng)
    elif lang_type == "russian":
        driver.get(url_rus)
    else:
        raise pytest.UsageError("-- lang_type should be english or russian")
    yield driver
    print("\nQuit browser..")
    time.sleep(25)
    driver.quit()
