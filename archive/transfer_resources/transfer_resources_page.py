from src.pages.base_page import BasePage
from archive.transfer_resources.locators import TransferResourcesLocators


class TransferResourcesPage(BasePage):
    def should_be_opened(self) -> None:
        # TODO: assert that Transfer resources page is opened.
        raise NotImplementedError

    def input_recipient_phone(self, phone: str) -> None:
        # TODO: input recipient phone number.
        raise NotImplementedError

    def input_gb_amount(self, amount: str) -> None:
        # TODO: input GB amount, for example "0.5".
        raise NotImplementedError

    def submit_transfer(self) -> None:
        # TODO: tap transfer button.
        raise NotImplementedError

    def confirmation_sheet_should_be_visible(self, recipient_phone: str, amount: str) -> None:
        # TODO: assert confirmation bottom sheet text.
        raise NotImplementedError

    def confirm_transfer(self) -> None:
        # TODO: confirm transfer from bottom sheet.
        raise NotImplementedError

    def return_to_transfer_page(self) -> None:
        # TODO: return from success screen to transfer resources page.
        raise NotImplementedError

    def cancel_transfer(self) -> None:
        # TODO: cancel transfer during allowed cancellation window.
        raise NotImplementedError

    def cancellation_should_be_successful(self) -> None:
        # TODO: assert successful cancellation state/snackbar.
        raise NotImplementedError
