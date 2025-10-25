import pytest
from tests.test_data import TEST_USERS, TEST_FORM_DATA, EXPECTED_MESSAGES
from Pages.login_page import LoginPage
from Pages.dashboard_page import DashboardPage
from config import BASE_URL

@pytest.mark.login_suite
def test_login_with_test_data(driver):
    """Example: Test login using test_data.py"""
    
    print("\n--- Test: Login with test data ---")
    
    # Get test data
    user_data = TEST_USERS["valid_user"]
    
    # Initialize page object
    login_page = LoginPage(driver, BASE_URL)
    dashboard_page = DashboardPage(driver, BASE_URL)
    
    # Perform login
    login_page.login(user_data["email"], user_data["password"])
    
    # Verify
    dashboard_page.wait_for_url_contains("/dashboard")
    assert dashboard_page.is_sidebar_displayed()
    
    print("--- Test: Login successful with test data ---")

@pytest.mark.login_suite
def test_invalid_login_with_test_data(driver):
    """Example: Test invalid login using test_data.py"""
    
    print("\n--- Test: Invalid login with test data ---")
    
    # Get test data
    user_data = TEST_USERS["invalid_user"]
    
    # Initialize page object
    login_page = LoginPage(driver, BASE_URL)
    
    # Perform login
    login_page.login(user_data["email"], user_data["password"])
    
    # Verify error
    assert login_page.is_error_displayed(), "Error message should be displayed"
    
    print("--- Test: Invalid login handled correctly ---")

@pytest.mark.example_suite
def test_environment_config(logged_in_driver):
    """Example: Test showing environment configuration"""
    
    print("\n--- Test: Environment configuration ---")
    from config import ENVIRONMENT, BASE_URL
    
    print(f"Current Environment: {ENVIRONMENT}")
    print(f"Base URL: {BASE_URL}")
    
    # Navigate to dashboard
    logged_in_driver.get(BASE_URL + "/dashboard")
    
    print("--- Test: Environment config working ---")

@pytest.mark.example_suite
def test_screenshot_on_failure_demo(logged_in_driver):
    """Example: This test will fail and take screenshot automatically"""
    
    print("\n--- Test: Screenshot on failure demo ---")
    
    # This will fail intentionally to demonstrate screenshot feature
    # Comment out the line below to make test pass
    assert False, "Intentional failure to demonstrate screenshot capture"
    
    print("--- Test: This line won't be reached ---")
