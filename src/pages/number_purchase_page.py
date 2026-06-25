from src.pages.base_page import BasePage
from src.pages.locators import NumberPurchaseLocators


class NumberPurchasePage(BasePage):
    def should_be_opened(self) -> None:
        # TODO: assert that number purchase page is opened.
        raise NotImplementedError

    def choose_available_number(self) -> str:
        # TODO: choose a price chip, then choose any available number and return selected number text.
        raise NotImplementedError

    def continue_order(self) -> None:
        # TODO: continue order after number selection.
        raise NotImplementedError
