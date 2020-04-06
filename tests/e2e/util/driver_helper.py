from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException, \
    ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import settings


class DriverHelper:
    def __init__(self, browser):
        self.browser = browser
        self.explicit_wait_time_ms = settings.EXPLICIT_WAIT_TIME_MS
        self.retry_wait_time_ms = 250
        self.retry_attempt = 10

    def wait_for_element(self, locator_type, element_locator, element_label):
        """
        This method waits for the presence of a given element within a specified time frame.
        If element is not present in the DOM a timeout exception is thrown.
        :return:
        """

        try:
            wait = WebDriverWait(self.browser, self.explicit_wait_time_ms)
            web_element = wait.until(EC.presence_of_element_located((locator_type, element_locator)))

            return web_element
        except TimeoutException:
            print("Can't find element in time: {}".format(element_label))
        # except NoSuchElementException:
        #     print("Can't find element: {}".format(element_label))

    def enter_text(self, locator_type, element_locator, text, element_label):
        """
        This method sends text characters to a text field.
        If element is not present in the DOM an exception is thrown.
        :return:
        """

        web_element = self.wait_for_element(locator_type, element_locator, element_label)

        try:
            web_element.click()
            web_element.clear()
            web_element.send_keys(text)
        except ElementNotInteractableException:
            print("Can't send text to element: {}".format(element_label))

    def click_element(self, locator_type, element_locator, element_label):
        """
        This method clicks on an element in the DOM.
        :return:
        """

        web_element = self.wait_for_element(locator_type, element_locator, element_label)

        try:
            web_element.click()

        except ElementClickInterceptedException:
            print("Can't click element: {}".format(element_label))

    def get_element_text(self, locator_type, element_locator, element_label):
        """
        This method returns the text value of an element in the DOM
        :param locator_type: By
        :param element_locator: string
        :param element_label: string
        :return: Element's text value
        """

        web_element = self.wait_for_element(locator_type, element_locator, element_label)

        try:
            element_text = web_element.text

            return element_text

        except NoSuchElementException:
            print("Can't get element text: {}".format(element_label))
