from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages import base_page


class DashboardPage(base_page.BasePage):
    dashboard_locator = (By.XPATH, '//h6[text()="Dashboard"]')

    def __init__(self, driver):
        super().__init__(driver)

    def is_dashboard_header_visible(self):
        # Wait until the URL changes to include dashboard
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("/dashboard")
        )
        # Wait for the dashboard header to be fully visible
        element = self.wait_for_element(self.dashboard_locator)
        return element.is_displayed()