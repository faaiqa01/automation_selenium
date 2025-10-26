from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

class LoginPage(BasePage):
    """Page Object Model for Login page."""
    
    # Locators
    LOGIN_LINK = (By.LINK_TEXT, "Login")
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, "login-button")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")
    
    def __init__(self, driver, base_url):
        """
        Initialize login page.
        
        Args:
            driver: Selenium WebDriver instance
            base_url: Base URL of the application
        """
        super().__init__(driver)
        self.base_url = base_url
    
    def navigate_to_login(self):
        """Navigate to the application and click login link."""
        self.navigate_to(self.base_url)
        self.click(*self.LOGIN_LINK)
    
    def enter_email(self, email):
        """
        Enter email address.
        
        Args:
            email: Email address string
        """
        self.input_text(*self.EMAIL_FIELD, email)
    
    def enter_password(self, password):
        """
        Enter password.
        
        Args:
            password: Password string
        """
        self.input_text(*self.PASSWORD_FIELD, password)
    
    def click_login_button(self):
        """Click the login button."""
        self.click(*self.LOGIN_BUTTON)
    
    def login(self, email, password):
        """
        Perform login with credentials.
        
        Args:
            email: Email address
            password: Password
        """
        self.navigate_to_login()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
    
    def get_error_message(self):
        """
        Get error message text.
        
        Returns:
            Error message string
        """
        return self.get_text(*self.ERROR_MESSAGE)
    
    def is_error_displayed(self):
        """
        Check if error message is displayed.
        
        Returns:
            Boolean
        """
        return self.is_displayed(*self.ERROR_MESSAGE)
