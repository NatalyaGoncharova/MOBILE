from src.pages.base_page import BasePage
from src.pages.locators import MainLocators


class MainPage(BasePage):
    def open_number_purchase(self) -> None:
        # TODO: open number purchase section from the authorized main page.
        raise NotImplementedError

    def refresh(self) -> None:
        # TODO: implement pull-to-refresh or app-specific refresh action.
        raise NotImplementedError
