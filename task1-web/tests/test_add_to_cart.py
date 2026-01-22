from conftest import login
from selenium.webdriver.common.by import By

def test_add_to_cart(driver):
    """Test adding an item to cart: core e-commerce functionality"""
    login(driver)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert cart_count == "1"
