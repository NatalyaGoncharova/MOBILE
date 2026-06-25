from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = 15):
        self.driver = driver
        self.timeout = timeout

    def find(self, locator: tuple):
        return WebDriverWait(self.driver, self.timeout).until(
            ec.visibility_of_element_located(locator)
        )

    def find_clickable(self, locator: tuple):
        return WebDriverWait(self.driver, self.timeout).until(
            ec.element_to_be_clickable(locator)
        )

    def click(self, locator: tuple) -> None:
        self.find_clickable(locator).click()

    def type_text(self, locator: tuple, value: str) -> None:
        element = self.find_clickable(locator)
        element.clear()
        element.send_keys(value)

    def text_of(self, locator: tuple) -> str:
        return self.find(locator).text

    def is_visible(self, locator: tuple, timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def wait_until_hidden(self, locator: tuple, timeout: int = 10) -> None:
        WebDriverWait(self.driver, timeout).until(ec.invisibility_of_element_located(locator))

    def back(self) -> None:
        self.driver.back()
