import pytest


TRANSFER_AMOUNT_GB = "0.5"


@pytest.mark.smoke
class TestTransferResources:
    def test_user_can_transfer_gb_and_cancel_transfer(
        self,
        login_page,
        main_page,
        transfer_resources_page,
        credentials,
        transfer_recipient,
    ):
        """Task 1: login, transfer resources, return and cancel transfer."""
        pytest.skip("TODO: implement this scenario using Page Objects")
