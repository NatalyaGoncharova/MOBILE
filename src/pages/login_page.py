from src.pages.base_page import BasePage
from src.pages.locators import LoginLocators


class LoginPage(BasePage):
    def login(self, phone: str, password: str) -> None:
        # TODO: implement login flow using LoginLocators.
        # Depending on app state, the flow may require PASSWORD_LOGIN_BUTTON or CONTINUE_BUTTON.
        raise NotImplementedError
