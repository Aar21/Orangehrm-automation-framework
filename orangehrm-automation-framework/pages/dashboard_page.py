from selenium.webdriver.common.by import By

from pages import base_page

class DashboardPage(base_page.BasePage):
    dashboard_locator = (By.XPATH,'//h6[text()="Dashboard"]')
    def __init__(self, driver):
        super().__init__(driver)

    def is_dashboard_header_visible(self):
        element = self.wait_for_element(self.dashboard_locator)
        return element.is_displayed()