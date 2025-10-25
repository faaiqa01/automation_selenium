# Test Data Management
# Pisahkan test data dari test code untuk maintainability yang lebih baik

# Test Users
TEST_USERS = {
    "valid_user": {
        "email": "user@example.com",
        "password": "password123"
    },
    "invalid_user": {
        "email": "invalid@example.com",
        "password": "wrongpassword"
    },
    "admin_user": {
        "email": "admin@example.com",
        "password": "adminpass123"
    }
}

# Test Form Data
TEST_FORM_DATA = {
    "contact_form": {
        "name": "Test User",
        "email": "test@example.com",
        "subject": "Test Subject",
        "message": "This is a test message"
    },
    "registration_form": {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "phone": "+1234567890",
        "address": "123 Test Street"
    }
}

# Test URLs (relative paths)
TEST_URLS = {
    "home": "/",
    "login": "/login",
    "dashboard": "/dashboard",
    "profile": "/profile",
    "settings": "/settings"
}

# Expected Messages
EXPECTED_MESSAGES = {
    "login_success": "Successfully logged in",
    "login_failed": "Invalid credentials",
    "form_success": "Form submitted successfully",
    "validation_error": "Please fill all required fields"
}

# Test Search Keywords
SEARCH_KEYWORDS = [
    "selenium",
    "automation",
    "testing",
    "python"
]
