from src.pages.base_page import BasePage
from src.pages.locators import RegistrationLocators


class RegistrationPage(BasePage):
    def should_be_opened_for_selected_number(self, phone_number: str) -> None:
        # TODO: assert that registration/order page is opened for selected number.
        raise NotImplementedError

    def proceed_to_iin_step(self) -> None:
        # TODO: pass required order screens until IIN input page.
        raise NotImplementedError

    def iin_input_should_be_visible(self) -> None:
        # TODO: assert IIN input field is visible.
        raise NotImplementedError
