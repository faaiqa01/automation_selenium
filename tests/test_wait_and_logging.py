import pytest
from selenium.webdriver.common.by import By
from utils.wait_helpers import CustomWaitHelpers, wait_for_loading_spinner
from utils.logger import CustomLogger, StepLogger
from config import BASE_URL

@pytest.mark.example_suite
def test_custom_wait_helpers_demo(logged_in_driver):
    """Example: Using custom wait helpers"""
    
    # Setup logger
    logger = CustomLogger.get_logger("WaitHelpersDemo")
    logger.info("=== Test: Custom Wait Helpers Demo ===")
    
    driver = logged_in_driver
    wait_helper = CustomWaitHelpers(driver, default_timeout=10)
    
    # Navigate to page
    logger.info(f"Navigating to: {BASE_URL}/dashboard")
    driver.get(BASE_URL + "/dashboard")
    
    # Wait for page load
    logger.info("Waiting for page to fully load...")
    if wait_helper.wait_for_page_load(timeout=20):
        logger.info("✓ Page loaded successfully")
    else:
        logger.warning("⚠ Page load timeout")
    
    # Wait for specific element
    logger.info("Waiting for sidebar element...")
    sidebar_locator = (By.ID, "sidebar")
    if wait_helper.wait_for_element_clickable(sidebar_locator):
        logger.info("✓ Sidebar is clickable")
    else:
        logger.error("✗ Sidebar not found or not clickable")
    
    # Wait for AJAX (if jQuery is used)
    logger.info("Waiting for AJAX requests to complete...")
    if wait_helper.wait_for_ajax_complete():
        logger.info("✓ All AJAX requests completed")
    
    logger.info("=== Test completed ===")

@pytest.mark.example_suite
def test_loading_spinner_example(logged_in_driver):
    """Example: Handling loading spinner"""
    
    logger = CustomLogger.get_logger("LoadingSpinnerDemo")
    logger.info("=== Test: Loading Spinner Demo ===")
    
    driver = logged_in_driver
    
    # Navigate to page with loading spinner
    logger.info(f"Navigating to: {BASE_URL}/slow-page")
    driver.get(BASE_URL + "/slow-page")
    
    # Wait for loading spinner to disappear
    spinner_locator = (By.CLASS_NAME, "loading-spinner")
    logger.info("Waiting for loading spinner to disappear...")
    
    wait_for_loading_spinner(driver, spinner_locator, timeout=30)
    logger.info("✓ Loading spinner disappeared")
    
    # Verify content loaded
    wait_helper = CustomWaitHelpers(driver)
    content_locator = (By.CLASS_NAME, "main-content")
    
    if wait_helper.wait_for_element_clickable(content_locator):
        logger.info("✓ Main content loaded successfully")
    
    logger.info("=== Test completed ===")

@pytest.mark.example_suite
def test_step_logger_demo(logged_in_driver):
    """Example: Using StepLogger for test steps"""
    
    # Initialize step logger
    step_log = StepLogger("StepLoggerDemo")
    
    driver = logged_in_driver
    
    step_log.step("Navigate to dashboard")
    driver.get(BASE_URL + "/dashboard")
    step_log.success("Dashboard page loaded")
    
    step_log.step("Verify sidebar is visible")
    wait_helper = CustomWaitHelpers(driver)
    sidebar_locator = (By.ID, "sidebar")
    
    if wait_helper.wait_for_element_clickable(sidebar_locator):
        step_log.success("Sidebar is visible and clickable")
    else:
        step_log.failure("Sidebar not found")
    
    step_log.step("Click on profile menu")
    step_log.info("Locating profile menu element...")
    profile_menu_locator = (By.ID, "profile-menu")
    
    if wait_helper.wait_for_element_clickable(profile_menu_locator):
        step_log.success("Profile menu found")
        # profile_menu.click() - commented for demo
    else:
        step_log.warning("Profile menu not found (expected for demo)")
    
    step_log.step("Verify profile page elements")
    step_log.info("Checking for user info...")
    step_log.success("Test completed successfully")

@pytest.mark.example_suite
def test_wait_for_dynamic_content(logged_in_driver):
    """Example: Wait for dynamic content loading"""
    
    logger = CustomLogger.get_logger("DynamicContentDemo")
    logger.info("=== Test: Dynamic Content Demo ===")
    
    driver = logged_in_driver
    wait_helper = CustomWaitHelpers(driver)
    
    # Navigate to page
    logger.info(f"Navigating to: {BASE_URL}/dynamic-page")
    driver.get(BASE_URL + "/dynamic-page")
    
    # Wait for specific number of items to load
    items_locator = (By.CLASS_NAME, "list-item")
    logger.info("Waiting for 10 items to load...")
    
    if wait_helper.wait_for_element_count(items_locator, count=10, timeout=15):
        logger.info("✓ All 10 items loaded")
    else:
        logger.warning("⚠ Timeout waiting for items")
    
    # Wait for specific text to appear
    success_msg_locator = (By.ID, "success-message")
    logger.info("Waiting for success message...")
    
    if wait_helper.wait_for_text_in_element(success_msg_locator, "Success", timeout=10):
        logger.info("✓ Success message displayed")
    
    # Wait for element attribute change (e.g., disabled -> enabled)
    button_locator = (By.ID, "submit-button")
    logger.info("Waiting for submit button to be enabled...")
    
    if wait_helper.wait_for_element_attribute(button_locator, "disabled", None, timeout=10):
        logger.info("✓ Submit button is enabled")
    
    logger.info("=== Test completed ===")

@pytest.mark.example_suite
def test_logger_levels_demo(logged_in_driver):
    """Example: Different logging levels"""
    
    logger = CustomLogger.get_logger("LoggerLevelsDemo", level=10)  # DEBUG level
    
    logger.debug("This is a DEBUG message - detailed information")
    logger.info("This is an INFO message - general information")
    logger.warning("This is a WARNING message - something unexpected")
    logger.error("This is an ERROR message - serious problem")
    logger.critical("This is a CRITICAL message - very serious problem")
    
    # Demonstrate in test context
    driver = logged_in_driver
    
    logger.info("Starting test execution...")
    logger.debug(f"Current URL: {driver.current_url}")
    logger.debug(f"Window size: {driver.get_window_size()}")
    
    try:
        driver.get(BASE_URL + "/dashboard")
        logger.info("Navigation successful")
    except Exception as e:
        logger.error(f"Navigation failed: {str(e)}")
    
    logger.info("Test execution completed")
