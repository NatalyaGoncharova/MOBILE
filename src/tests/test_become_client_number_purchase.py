import pytest


@pytest.mark.smoke
class TestBecomeClientNumberPurchase:
    def test_unauthorized_user_can_reach_iin_step_from_number_purchase(
        self,
        become_client_page,
        number_purchase_page,
        registration_page,
    ):
        """Task 2: without authorization, start number purchase and reach IIN input."""
        pytest.skip("TODO: implement this scenario using Page Objects")
