from selenium.webdriver.common.by import By
from Pages.base_page import BasePage

class DashboardPage(BasePage):
    """Page Object Model for Dashboard page."""
    
    # Locators
    SIDEBAR = (By.ID, "sidebar")
    PAGE_TITLE = (By.TAG_NAME, "h1")
    USER_MENU = (By.CLASS_NAME, "user-menu")
    LOGOUT_BUTTON = (By.LINK_TEXT, "Logout")
    NOTIFICATION_ICON = (By.ID, "notification-icon")
    
    def __init__(self, driver, base_url):
        """
        Initialize dashboard page.
        
        Args:
            driver: Selenium WebDriver instance
            base_url: Base URL of the application
        """
        super().__init__(driver)
        self.base_url = base_url
        self.dashboard_url = f"{base_url}/dashboard"
    
    def navigate_to_dashboard(self):
        """Navigate to dashboard page."""
        self.navigate_to(self.dashboard_url)
    
    def is_sidebar_displayed(self):
        """
        Check if sidebar is displayed.
        
        Returns:
            Boolean
        """
        return self.is_displayed(*self.SIDEBAR)
    
    def get_page_title(self):
        """
        Get dashboard page title.
        
        Returns:
            Page title string
        """
        return self.get_text(*self.PAGE_TITLE)
    
    def click_user_menu(self):
        """Click user menu."""
        self.click(*self.USER_MENU)
    
    def logout(self):
        """Perform logout action."""
        self.click_user_menu()
        self.click(*self.LOGOUT_BUTTON)
    
    def is_notification_displayed(self):
        """
        Check if notification icon is displayed.
        
        Returns:
            Boolean
        """
        return self.is_displayed(*self.NOTIFICATION_ICON)
