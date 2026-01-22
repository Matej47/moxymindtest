from appium import webdriver
from appium.options.android import UiAutomator2Options

def create_driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "Android Emulator"
    options.automation_name = "UiAutomator2"

    # Google Clock (Pixel emulator)
    options.app_package = "com.google.android.deskclock"
    options.app_activity = "com.android.deskclock.DeskClock"  # fixed launcher activity

    # IMPORTANT: prevent reinstall/reset errors
    options.no_reset = True

    return webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )
