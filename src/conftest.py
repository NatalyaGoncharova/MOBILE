import os

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv

from src.pages.login_page import LoginPage
from src.pages.main_page import MainPage
from src.pages.become_client_page import BecomeClientPage
from src.pages.number_purchase_page import NumberPurchasePage
from src.pages.registration_page import RegistrationPage


load_dotenv()


@pytest.fixture(scope="session")
def appium_server_url() -> str:
    return os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723")


@pytest.fixture
def driver(appium_server_url):
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.platform_version = os.getenv("ANDROID_PLATFORM_VERSION")
    options.device_name = os.getenv("ANDROID_DEVICE_NAME", "Android Emulator")
    options.app = os.getenv("ANDROID_APP_PATH", "app/tele2/android/app.apk")
    options.automation_name = "UiAutomator2"
    options.no_reset = False

    driver = webdriver.Remote(appium_server_url, options=options)
    yield driver
    driver.quit()


@pytest.fixture
def credentials():
    return {
        "phone": os.getenv("TELE2_PHONE"),
        "password": os.getenv("TELE2_PASSWORD"),
    }


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def become_client_page(driver):
    return BecomeClientPage(driver)


@pytest.fixture
def number_purchase_page(driver):
    return NumberPurchasePage(driver)


@pytest.fixture
def registration_page(driver):
    return RegistrationPage(driver)
