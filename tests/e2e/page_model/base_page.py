class BasePage:
    def __init__(self, driver, visit=False):
        self.driver = driver

        if visit:
            self.driver.get(self.url)


    @property
    def url(self):
        """
        This method returns the homepage url.
        :return: Homepgae url
        """
        return 'https://uat.ormuco.com'

    @property
    def verify_welcome_page(self):
        """
        This method verifies homepage is loaded by verifying the page title
        :return: Instance of webpage
        """
        actual_title = 'Portal - Ormuco'
        return self
