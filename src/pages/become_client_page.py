from src.pages.base_page import BasePage
from src.pages.locators import BecomeClientLocators


class BecomeClientPage(BasePage):
    def open(self) -> None:
        # TODO: open "Become a client" flow from unauthorized app state.
        raise NotImplementedError

    def choose_almaty_city(self) -> None:
        # TODO: select Almaty city and confirm it.
        raise NotImplementedError

    def should_be_opened(self) -> None:
        # TODO: assert that "Become a client" page is opened.
        raise NotImplementedError

    def choose_number_purchase(self) -> None:
        # TODO: select number purchase option.
        raise NotImplementedError
