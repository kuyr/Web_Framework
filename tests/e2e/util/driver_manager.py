import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import settings


class DriverManager(unittest.TestCase):
    """
    This class is for instantiating web driver instances and launching the browser.
    """

    def setUp(self):
        """
        This method instantiates the web driver instance
        """
        self.browser = self.start_browser(settings.BROWSER)
        self.browser.maximize_window()

        self.browser.get(settings.URL)

    def start_browser(self, browser_name):
        """
        This method creates a browser
        :return: browser object
        """

        if browser_name.lower() == "chrome":
            print("##### Initializing the webdriver #####")
            options = webdriver.ChromeOptions()
            options.add_argument("--disable-infobars")
            browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
        elif browser_name.lower() == "firefox":
            print("##### Initializing the webdriver #####")
            options = webdriver.FirefoxOptions()
            options.add_argument("--disable-infobars")
            browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
        else:
            raise Exception("'{}' browser not supported".format(browser_name))
        return browser

    def tearDown(self):
        """
        This method quits the browser
        """
        print("##### Removing the webdriver #####")
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
