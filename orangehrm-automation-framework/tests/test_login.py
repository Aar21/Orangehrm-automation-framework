import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.json_reader import get_test_data

@pytest.mark.usefixtures("setup_teardown")
class TestLogin:

    def test_valid_login(self):
        data = get_test_data("credentials.json")
        username = data["valid_user"]["username"]
        password = data["valid_user"]["password"]

        login_page = LoginPage(self.driver)
        dashboard_page = DashboardPage(self.driver)

        login_page.login(username, password)

        assert dashboard_page.is_dashboard_header_visible() == True, "Login Failed"

    def test_invalid_login(self):
        data = get_test_data("credentials.json")
        username = data["invalid_user"]["username"]
        password = data["invalid_user"]["password"]

        login_page = LoginPage(self.driver)
        dashboard_page = DashboardPage(self.driver)

        login_page.login(username, password)

        error_text = login_page.get_error_message()
        assert "Invalid credentials" in error_text, f"Expected 'Invalid credentials' error, but got: {error_text}"