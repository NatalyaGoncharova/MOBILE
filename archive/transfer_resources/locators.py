from appium.webdriver.common.appiumby import AppiumBy


class TransferResourcesLocators:
    TITLE = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("toolbarWidgetTitle").text("Перевод ресурсов")',
    )
    RECIPIENT_PHONE_INPUT = (AppiumBy.ID, "shareGBSScreenRecipientField")
    GB_AMOUNT_INPUT = (AppiumBy.ID, "shareGBSScreenAmountField")
    TRANSFER_BUTTON = (AppiumBy.ID, "shareMinutesButton")
    CONFIRMATION_SHEET = (AppiumBy.ID, "design_bottom_sheet")
    CONFIRMATION_TEXT = (AppiumBy.ID, "bottomSheetSubTitle")
    CONFIRM_BUTTON = (AppiumBy.ID, "groupButtonPrimaryButton")
    BACK_TO_TRANSFER_BUTTON = (AppiumBy.ID, "groupButtonSecondaryButton")
    CANCEL_TRANSFER_BUTTON = (AppiumBy.ID, "shareMinutesButton")
    CANCELLATION_SUCCESS_MESSAGE = (AppiumBy.ID, "snackbarWidgetText")
