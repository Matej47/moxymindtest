from selenium.webdriver.common.by import By

def test_login_failure(driver):
    """Test login with wrong credentials: essential to ensure security"""
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("wrong_user")
    driver.find_element(By.ID, "password").send_keys("wrong_pass")
    driver.find_element(By.ID, "login-button").click()
    error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    assert "Username and password do not match" in error_message
