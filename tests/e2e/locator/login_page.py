from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL = By.ID, "username"
    PASSWORD = By.ID, "password"
    SIGN_IN_BUTTON = By.XPATH, "//*[@id='login_form']/ng-form/div[3]/div[2]/button"
    WARNING_LABEL = By.XPATH, "//*[@class='warning' and text() != '']"
