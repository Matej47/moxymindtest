from conftest import login
from selenium.webdriver.common.by import By

def test_add_to_cart(driver):
    """Verify users can add an item to the cart.

    Essential because adding to cart is a primary action in any
    e-commerce flow. If this breaks, users cannot progress toward checkout. No money :(
    """
    login(driver)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert cart_count == "1"
