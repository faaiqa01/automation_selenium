import pytest
from selenium.webdriver.common.by import By
from page_objects.login_page import LoginPage
from page_objects.dashboard_page import DashboardPage
from config import BASE_URL, USERNAME, PASSWORD

@pytest.mark.login_suite
def test_login_with_valid_credentials(driver):
    """Test login with valid credentials using Page Object Model."""
    
    print("\n--- Test: Login with valid credentials (POM) ---")
    
    # Initialize page objects
    login_page = LoginPage(driver, BASE_URL)
    dashboard_page = DashboardPage(driver, BASE_URL)
    
    # Perform login
    login_page.login(USERNAME, PASSWORD)
    
    # Verify successful login
    dashboard_page.wait_for_url_contains("/dashboard")
    assert dashboard_page.is_sidebar_displayed(), "Sidebar should be visible after login"
    
    print("--- Test: Login successful (POM) ---")

@pytest.mark.login_suite
def test_login_with_invalid_credentials(driver):
    """Test login with invalid credentials using Page Object Model."""
    
    print("\n--- Test: Login with invalid credentials (POM) ---")
    
    # Initialize page objects
    login_page = LoginPage(driver, BASE_URL)
    
    # Perform login with invalid credentials
    login_page.login("invalid@email.com", "wrongpassword")
    
    # Verify error message is displayed
    assert login_page.is_error_displayed(), "Error message should be displayed"
    print(f"Error message: {login_page.get_error_message()}")
    
    print("--- Test: Invalid login handled correctly (POM) ---")

@pytest.mark.dashboard_suite
def test_dashboard_elements(logged_in_driver):
    """Test dashboard page elements using Page Object Model."""
    
    print("\n--- Test: Dashboard elements (POM) ---")
    
    # Initialize page object
    dashboard_page = DashboardPage(logged_in_driver, BASE_URL)
    
    # Navigate to dashboard
    dashboard_page.navigate_to_dashboard()
    
    # Verify elements
    assert dashboard_page.is_sidebar_displayed(), "Sidebar should be visible"
    print(f"Page title: {dashboard_page.get_page_title()}")
    
    print("--- Test: Dashboard elements verified (POM) ---")

@pytest.mark.login_suite
def test_logout(logged_in_driver):
    """Test logout functionality using Page Object Model."""
    
    print("\n--- Test: Logout (POM) ---")
    
    # Initialize page object
    dashboard_page = DashboardPage(logged_in_driver, BASE_URL)
    
    # Navigate to dashboard
    dashboard_page.navigate_to_dashboard()
    
    # Perform logout
    dashboard_page.logout()
    
    # Verify logout (adjust based on your app behavior)
    dashboard_page.wait_for_url_contains("/login")
    
    print("--- Test: Logout successful (POM) ---")
