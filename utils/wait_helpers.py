from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class CustomWaitHelpers:
    """Custom wait helper functions for common waiting scenarios."""
    
    def __init__(self, driver, default_timeout=10):
        """
        Initialize custom wait helpers.
        
        Args:
            driver: Selenium WebDriver instance
            default_timeout: Default timeout in seconds
        """
        self.driver = driver
        self.default_timeout = default_timeout
    
    def wait_until_element_disappears(self, locator, timeout=None):
        """
        Wait until element disappears from DOM (useful for loading spinners, overlays).
        
        Args:
            locator: Tuple of (By.TYPE, "value")
            timeout: Maximum wait time in seconds
            
        Returns:
            True if element disappeared, False otherwise
        """
        timeout = timeout or self.default_timeout
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    
    def wait_for_ajax_complete(self, timeout=None):
        """
        Wait until all jQuery AJAX requests are complete.
        
        Args:
            timeout: Maximum wait time in seconds
            
        Returns:
            True if AJAX completed, False otherwise
        """
        timeout = timeout or self.default_timeout
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(lambda driver: driver.execute_script("return jQuery.active == 0"))
            return True
        except TimeoutException:
            return False
        except Exception:
            # jQuery might not be loaded
            return True
    
    def wait_for_page_load(self, timeout=None):
        """
        Wait until page is fully loaded (document.readyState = complete).
        
        Args:
            timeout: Maximum wait time in seconds
            
        Returns:
            True if page loaded, False otherwise
        """
        timeout = timeout or self.default_timeout
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
            return True
        except TimeoutException:
            return False
    
    def wait_for_element_attribute(self, locator, attribute, value, timeout=None):
        """
        Wait until element attribute has specific value.
        
        Args:
            locator: Tuple of (By.TYPE, "value")
            attribute: Attribute name (e.g., "class", "disabled")
            value: Expected attribute value
            timeout: Maximum wait time in seconds
            
        Returns:
            True if attribute matches, False otherwise
        """
        timeout = timeout or self.default_timeout
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(lambda driver: driver.find_element(*locator).get_attribute(attribute) == value)
            return True
        except TimeoutException:
            return False
    
    def wait_for_element_count(self, locator, count, timeout=None):
        """
        Wait until number of elements matches expected count.
        
        Args:
            locator: Tuple of (By.TYPE, "value")
            count: Expected number of elements
            timeout: Maximum wait time in seconds
            
        Returns:
            True if count matches, False otherwise
        """
        timeout = timeout or self.default_timeout
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(lambda driver: len(driver.find_elements(*locator)) == count)
            return True
        except TimeoutException:
            return False
    
    def wait_for_element_clickable(self, locator, timeout=None):
        """
        Wait until element is clickable (visible and enabled).
        
        Args:
            locator: Tuple of (By.TYPE, "value")
            timeout: Maximum wait time in seconds
            
        Returns:
            WebElement if clickable, None otherwise
        """
        timeout = timeout or self.default_timeout
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.element_to_be_clickable(locator))
            return element
        except TimeoutException:
            return None
    
    def wait_for_text_in_element(self, locator, text, timeout=None):
        """
        Wait until element contains specific text.
        
        Args:
            locator: Tuple of (By.TYPE, "value")
            text: Expected text in element
            timeout: Maximum wait time in seconds
            
        Returns:
            True if text present, False otherwise
        """
        timeout = timeout or self.default_timeout
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.text_to_be_present_in_element(locator, text))
            return True
        except TimeoutException:
            return False
    
    def wait_for_url_contains(self, partial_url, timeout=None):
        """
        Wait until URL contains partial string.
        
        Args:
            partial_url: Partial URL string
            timeout: Maximum wait time in seconds
            
        Returns:
            True if URL contains string, False otherwise
        """
        timeout = timeout or self.default_timeout
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.url_contains(partial_url))
            return True
        except TimeoutException:
            return False
    
    def wait_for_alert_present(self, timeout=None):
        """
        Wait until alert is present.
        
        Args:
            timeout: Maximum wait time in seconds
            
        Returns:
            Alert object if present, None otherwise
        """
        timeout = timeout or self.default_timeout
        try:
            wait = WebDriverWait(self.driver, timeout)
            alert = wait.until(EC.alert_is_present())
            return alert
        except TimeoutException:
            return None
    
    def wait_for_new_window(self, current_window_count, timeout=None):
        """
        Wait until new window/tab is opened.
        
        Args:
            current_window_count: Current number of windows
            timeout: Maximum wait time in seconds
            
        Returns:
            True if new window opened, False otherwise
        """
        timeout = timeout or self.default_timeout
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(lambda driver: len(driver.window_handles) > current_window_count)
            return True
        except TimeoutException:
            return False


# Standalone helper functions (alternative to class-based)

def wait_for_loading_spinner(driver, spinner_locator, timeout=10):
    """
    Wait for loading spinner to appear and disappear.
    
    Args:
        driver: Selenium WebDriver instance
        spinner_locator: Tuple of (By.TYPE, "value") for spinner
        timeout: Maximum wait time in seconds
    """
    try:
        # Wait for spinner to appear
        WebDriverWait(driver, 2).until(EC.presence_of_element_located(spinner_locator))
        # Wait for spinner to disappear
        WebDriverWait(driver, timeout).until(EC.invisibility_of_element_located(spinner_locator))
    except TimeoutException:
        # Spinner might not appear at all (fast loading)
        pass

def wait_for_element_stable(driver, locator, stable_time=1, timeout=10):
    """
    Wait until element position is stable (useful for animations).
    
    Args:
        driver: Selenium WebDriver instance
        locator: Tuple of (By.TYPE, "value")
        stable_time: Time in seconds element must be stable
        timeout: Maximum wait time in seconds
        
    Returns:
        True if element is stable, False otherwise
    """
    import time
    end_time = time.time() + timeout
    last_location = None
    stable_count = 0
    
    while time.time() < end_time:
        try:
            element = driver.find_element(*locator)
            current_location = element.location
            
            if last_location == current_location:
                stable_count += 0.1
                if stable_count >= stable_time:
                    return True
            else:
                stable_count = 0
            
            last_location = current_location
            time.sleep(0.1)
        except:
            return False
    
    return False
