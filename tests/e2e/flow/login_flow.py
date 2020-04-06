from tests.e2e.page_model.login_page import LoginPage
import settings


class LoginFlow:
    def __init__(self, browser):
        self.browser = browser

    def login_with_no_email_and_no_password(self):
        login_page = LoginPage(self.browser)
        login_page.login("", "")

        return login_page

    def login_with_wrong_email_and_wrong_password(self):
        login_page = LoginPage(self.browser)
        login_page.login(settings.INVALID_EMAIL, settings.INVALID_PASSWORD)

        return login_page
