import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.lang
def test_add_to_cart_button(browser):

    # поиск элемента на странице
    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, "//button[@class ='btn btn-lg btn-primary btn-add-to-basket']")))
    button = browser.find_element(By.XPATH, "//button[@class ='btn btn-lg btn-primary btn-add-to-basket']").text

    try:
        assert button == "Añadir al carrito", "Should be Añadir al carrito"
    except AssertionError:
        assert button == "Ajouter au panier", "Should be Ajouter au panier"
