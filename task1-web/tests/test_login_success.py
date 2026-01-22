from conftest import login
from selenium.webdriver.common.by import By

def test_login_success(driver):
    """Test login functionality: essential to access app features"""
    login(driver)
    # Verify we are on inventory page
    assert "inventory" in driver.current_url
    assert driver.find_element(By.CLASS_NAME, "inventory_list")
    