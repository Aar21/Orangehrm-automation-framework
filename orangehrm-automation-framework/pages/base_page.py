from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            lambda driver: driver.find_element(*locator)
        )

    def click_element(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    def enter_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

