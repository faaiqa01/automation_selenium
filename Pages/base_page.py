from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    """Base class for all page objects."""
    
    def __init__(self, driver):
        """
        Initialize base page.
        
        Args:
            driver: Selenium WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def find_element(self, by, value):
        """
        Find element with explicit wait.
        
        Args:
            by: Selenium By locator type
            value: Locator value
            
        Returns:
            WebElement
        """
        return self.wait.until(EC.presence_of_element_located((by, value)))
    
    def find_elements(self, by, value):
        """
        Find multiple elements.
        
        Args:
            by: Selenium By locator type
            value: Locator value
            
        Returns:
            List of WebElements
        """
        return self.driver.find_elements(by, value)
    
    def click(self, by, value):
        """
        Click element with explicit wait.
        
        Args:
            by: Selenium By locator type
            value: Locator value
        """
        element = self.wait.until(EC.element_to_be_clickable((by, value)))
        element.click()
    
    def input_text(self, by, value, text):
        """
        Input text into element.
        
        Args:
            by: Selenium By locator type
            value: Locator value
            text: Text to input
        """
        element = self.find_element(by, value)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, by, value):
        """
        Get text from element.
        
        Args:
            by: Selenium By locator type
            value: Locator value
            
        Returns:
            Element text
        """
        element = self.find_element(by, value)
        return element.text
    
    def is_displayed(self, by, value):
        """
        Check if element is displayed.
        
        Args:
            by: Selenium By locator type
            value: Locator value
            
        Returns:
            Boolean
        """
        try:
            element = self.find_element(by, value)
            return element.is_displayed()
        except:
            return False
    
    def wait_for_url(self, url, timeout=10):
        """
        Wait for URL to match.
        
        Args:
            url: Expected URL
            timeout: Maximum wait time in seconds
        """
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.url_to_be(url))
    
    def wait_for_url_contains(self, partial_url, timeout=10):
        """
        Wait for URL to contain partial string.
        
        Args:
            partial_url: Partial URL string
            timeout: Maximum wait time in seconds
        """
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.url_contains(partial_url))
    
    def get_current_url(self):
        """
        Get current page URL.
        
        Returns:
            Current URL string
        """
        return self.driver.current_url
    
    def navigate_to(self, url):
        """
        Navigate to URL.
        
        Args:
            url: URL to navigate to
        """
        self.driver.get(url)
