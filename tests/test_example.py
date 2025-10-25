import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL

@pytest.mark.example_suite
def test_example_navigation(logged_in_driver):
    """Example test case - navigate to a page."""
    driver = logged_in_driver
    
    print("\n--- Test: Navigating to example page ---")
    
    # Navigate to a page
    driver.get(BASE_URL + "/example-page")
    
    # Wait for element to be visible
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "example-element"))
    )
    
    # Assertions
    assert element.is_displayed(), "Element should be visible"
    print("--- Test: Navigation successful ---")

@pytest.mark.example_suite
def test_example_form_submission(logged_in_driver):
    """Example test case - submit a form."""
    driver = logged_in_driver
    
    print("\n--- Test: Submitting example form ---")
    
    driver.get(BASE_URL + "/form-page")
    
    # Fill form
    input_field = driver.find_element(By.ID, "input-field")
    input_field.send_keys("Test Data")
    
    # Submit
    submit_button = driver.find_element(By.ID, "submit-button")
    submit_button.click()
    
    # Verify success
    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "success-message"))
    )
    
    assert "Success" in success_message.text
    print("--- Test: Form submitted successfully ---")
