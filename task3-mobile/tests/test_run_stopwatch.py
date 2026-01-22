import pytest
from driver.android_driver import create_driver
import time
from appium.webdriver.common.appiumby import AppiumBy

@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

def test_stopwatch_start(driver):
    timer_tab = driver.find_element(
        AppiumBy.ID, "com.google.android.deskclock:id/tab_menu_stopwatch"
    )
    timer_tab.click()
    
    # Locate the Start button
    start_button = driver.find_element(
        AppiumBy.ID, "com.google.android.deskclock:id/fab"
    )
    
    # Locate stopwatch time text
    time_text = driver.find_element(
        AppiumBy.ID, "com.google.android.deskclock:id/stopwatch_time_text"
    )
    
    initial_time = time_text.text
    print(f"Initial time: {initial_time}")
    
    # Start the stopwatch
    start_button.click()
    
    # Wait
    time.sleep(1)
    
    # Stop the stopwatch
    start_button.click()