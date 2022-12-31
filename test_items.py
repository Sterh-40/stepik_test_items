import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.lang
def test_lang(driver):
    #поиск элемента на странице
    WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, "//button[@class ='btn btn-lg btn-primary btn-add-to-basket']")))










