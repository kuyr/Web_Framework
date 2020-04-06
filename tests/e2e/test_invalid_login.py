from tests.e2e.util.driver_manager import DriverManager
from tests.e2e.flow.login_flow import LoginFlow


class TestInvalidLogin(DriverManager):

    def test_no_email_and_no_password_login(self):
        """
        This method attempts to login without entering email and password
        """

        actual_title = "Portal - Ormuco"
        actual_warning_text = "The user or password is incorrect."

        login_flow = LoginFlow(self.browser)
        login_page = login_flow.login_with_no_email_and_no_password()

        expected_title = login_page.get_title()
        expected_warning_text = login_page.get_warning_label_text()

        assert actual_title == expected_title
        assert expected_warning_text == actual_warning_text

    def test_incorrect_email_and_incorrect_password_login(self):
        """
        This method attempts to login by entering wrong credentials
        """

        actual_title = "Portal - Ormuco"
        actual_warning_text = "The user or password is incorrect."

        login_flow = LoginFlow(self.browser)
        login_page = login_flow.login_with_wrong_email_and_wrong_password()

        expected_title = login_page.get_title()
        expected_warning_text = login_page.get_warning_label_text()

        assert actual_title == expected_title
        assert expected_warning_text == actual_warning_text
