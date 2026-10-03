from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class LoginPage(BasePage):
    username_field = (By.NAME,"username")
    password_field = (By.NAME,"password")
    login_btn = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        super().__init__(driver)

    def type_username(self, username):
        self.enter_text(self.username_field, username)

    def type_password(self, password):
        self.enter_text(self.password_field, password)

    def click_login_btn(self):
        self.click_element(self.login_btn)

    def login(self, username, password):
        self.type_username(username)
        self.type_password(password)
        self.click_login_btn()

    error_message_locator = (By.XPATH, "//p[contains(@class, 'oxd-alert-content-text')]")
    def get_error_message(self):
        element = self.wait_for_element(self.error_message_locator)
        return element.text