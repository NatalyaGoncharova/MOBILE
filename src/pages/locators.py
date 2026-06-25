from appium.webdriver.common.appiumby import AppiumBy


class LoginLocators:
    PHONE_INPUT = (AppiumBy.ID, "LoginScreenPhoneTextField")
    PASSWORD_LOGIN_BUTTON = (AppiumBy.ID, "LoginScreenPasswordEnterButton")
    CONTINUE_BUTTON = (AppiumBy.ID, "kz.tele2.app:id/loginButtonView")
    PASSWORD_INPUT = (AppiumBy.ID, "kz.tele2.app:id/passEditTextView")
    SUBMIT_BUTTON = (AppiumBy.ID, "kz.tele2.app:id/loginButton")


class MainLocators:
    NUMBER_PURCHASE_BUTTON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().textContains("Купить номер")',
    )
    REFRESH_CONTAINER = (AppiumBy.ID, "mainRefreshContainer")


class BecomeClientLocators:
    BECOME_CLIENT_BUTTON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Купите номер или перейдите со своим")',
    )
    CITY_ALMATY = (AppiumBy.ID, "SelectCityScreenАлматы")
    CITY_ASTANA = (AppiumBy.ID, "SelectCityScreenАстана")
    CITY_CONFIRM_BUTTON = (AppiumBy.ID, "SelectCityScreenMainButton")
    TITLE = (AppiumBy.ID, "kz.tele2.app:id/fragment_mnp_main_page_topAppBar")
    NUMBER_PURCHASE_BUTTON = (
        AppiumBy.ID,
        "kz.tele2.app:id/fragment_mnp_main_page_mobile_number_sales_banner",
    )


class NumberPurchaseLocators:
    TITLE = (AppiumBy.ID, "kz.tele2.app:id/fragment_mobile_numbers_catalogue_title")
    PRICE_CHIP = (AppiumBy.ID, "kz.tele2.app:id/item_chips_text")
    FIRST_AVAILABLE_NUMBER = (AppiumBy.ID, "kz.tele2.app:id/item_mobile_number")
    REGISTRATION_TITLE = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Оформление")',
    )
    CONTINUE_BUTTON = (AppiumBy.ID, "MobileNumberSalesCartScreenPayButton")


class RegistrationLocators:
    TITLE = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Регистрация номера")',
    )
    SELECTED_NUMBER = (AppiumBy.ID, "MobileNumberSalesCartScreenSellingPhoneNumber")
    SIM_CARD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("dataContentTitle").text("SIM-карта")',
    )
    TARIFF = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("dataContentTitle").text("Тариф")',
    )
    ISSUE_METHOD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("dataContentTitle").text("Способ выдачи")',
    )
    CONTACT_PHONE_INPUT = (AppiumBy.ID, "MobileNumberSalesCartScreenComponentTextField")
    PAYMENT_METHOD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("dataContentTitle").text("Оплата")',
    )
    CONTINUE_BUTTON = (AppiumBy.ID, "MobileNumberSalesCartScreenPayButton")
    IIN_SCREEN = (AppiumBy.ID, "IinScreenColumn")
    IIN_INPUT = (AppiumBy.CLASS_NAME, "android.widget.EditText")
