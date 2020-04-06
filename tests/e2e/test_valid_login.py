from tests.e2e.util.driver_manager import DriverManager
from tests.e2e.flow.login_flow import LoginFlow


class TestValidLogin(DriverManager):

    def test_valid_login(self):
        """
        This method was only created to properly simulate running tests in parallel.
        As a result method name is misleading.
        :return:
        """

        actual_title = "Portal - Ormuco"
        actual_warning_text = "The user or password is incorrect."

        login_flow = LoginFlow(self.browser)
        login_page = login_flow.login_with_no_email_and_no_password()

        expected_title = login_page.get_title()
        expected_warning_text = login_page.get_warning_label_text()

        assert actual_title == expected_title
        assert expected_warning_text == actual_warning_text


# python -m unittest discover
#
# Command to run test in parallel: py.test -n 2

# What is left:
# 1. Reporting
# 2. Catching error and quitting test properly
# 3. Include .gitignore file : ignore .env file
# 4. Explain choice of tool for project: README.md
# 5. Ensure all functions have comment
# 6. Check code based on test evaluation criteria again e.g. method names, method description, etc...
