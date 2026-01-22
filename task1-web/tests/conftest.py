import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

USERNAME = os.getenv("SAUCE_USERNAME")
PASSWORD = os.getenv("SAUCE_PASSWORD")

def _create_firefox_options():
    options = webdriver.FirefoxOptions()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    options.add_argument("--disable-notifications")
    options.add_argument("--private")
    options.set_preference("signon.rememberSignons", False)
    options.set_preference("signon.autofillForms", False)
    options.set_preference("network.http.prompt-temp-redirect", False)
    options.set_preference("privacy.popups.showBrowserMessage", False)
    return options

@pytest.fixture
def driver():
    options = _create_firefox_options()
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
    yield driver
    driver.quit()

# login helper
def login(driver, username=USERNAME, password=PASSWORD):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
