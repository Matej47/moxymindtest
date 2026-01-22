from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import login

def test_checkout(driver):
    """Test checkout process: essential for completing purchases"""
    login(driver)

    # Add item to cart
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    # Step 4: Wait for Checkout button to appear and click it
    checkout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    )
    checkout_button.click()

    # Wait until checkout form is visible
    first_name_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "first-name"))
    )
    first_name_input.send_keys("Test")

    driver.find_element(By.ID, "last-name").send_keys("User")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()

    # Check we are on the overview page
    assert "checkout-step-two" in driver.current_url
