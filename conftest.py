import time
import pytest
from selenium import webdriver

url_es = "http://selenium1py.pythonanywhere.com/es/catalogue/coders-at-work_207/"
url_fr = "http://selenium1py.pythonanywhere.com/fr/catalogue/coders-at-work_207/"

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='None', help="Choose language: es or fr")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption('--language')
    print("\nStart browser test..")
    browser = webdriver.Chrome()
    if language == "es":
        browser.get(url_es)
    elif language == "fr":
        browser.get(url_fr)
    else:
        raise pytest.UsageError("-- language should be es or fr")
    yield browser
    print("\nQuit browser..")
    time.sleep(10)
    browser.quit()
