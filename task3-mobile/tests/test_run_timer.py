import pytest
from driver.android_driver import create_driver
from appium.webdriver.common.appiumby import AppiumBy
import time

@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

def test_toggle_alarm(driver):
    # Make sure we're on the Alarm tab
    alarm_tab = driver.find_element(
        AppiumBy.ID, "com.google.android.deskclock:id/tab_menu_alarm"
    )
    alarm_tab.click()
    time.sleep(1)  # wait for UI to settle

    # Locate the first alarm's toggle switch
    alarm_switch = driver.find_element(
        AppiumBy.ID, "com.google.android.deskclock:id/onoff"
    )

    # Get current state
    initial_state = alarm_switch.get_attribute("checked")
    print(f"Initial alarm state: {initial_state}")

    # Toggle the alarm
    alarm_switch.click()
    time.sleep(1)

    # Verify state changed
    new_state = alarm_switch.get_attribute("checked")
    print(f"New alarm state: {new_state}")
    assert new_state != initial_state, "Alarm state did not change after clicking"

    # Toggle back to original state
    alarm_switch.click()
    time.sleep(1)
    restored_state = alarm_switch.get_attribute("checked")
    print(f"Restored alarm state: {restored_state}")
    assert restored_state == initial_state, "Alarm state did not restore properly"
