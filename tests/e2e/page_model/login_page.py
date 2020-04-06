from tests.e2e.locator.login_page import LoginPageLocators
from tests.e2e.util.driver_helper import DriverHelper


class LoginPage:
    def __init__(self, browser):
        self.browser = browser
        self.title = "Portal - Ormuco"
        self.verify_login_page()
        self.driver_helper = DriverHelper(self.browser)

    def verify_login_page(self):
        """
        This method verifies login page is loaded by verifying the page title
        :return: Instance of web page
        """
        actual_title = self.browser.title
        assert actual_title == self.title, "Actual title '{}', should be same as '{}'".format(actual_title, self.title)

        return self

    def get_warning_label_text(self):
        return self.driver_helper.get_element_text(*LoginPageLocators.WARNING_LABEL, "Warning label")

    def get_title(self):
        return self.browser.title

    def enter_email(self, email):
        self.driver_helper.enter_text(*LoginPageLocators.EMAIL, email, "Email field")

    def enter_password(self, password):
        self.driver_helper.enter_text(*LoginPageLocators.PASSWORD, password, "Password field")

    def click_sign_in_button(self):
        self.driver_helper.click_element(*LoginPageLocators.SIGN_IN_BUTTON, "SIGN IN button")

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_sign_in_button()
