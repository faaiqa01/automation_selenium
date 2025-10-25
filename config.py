# File untuk menyimpan semua konfigurasi global
import os

# Environment Configuration
# Set environment via: set ENV=dev (Windows) or export ENV=dev (Linux/Mac)
ENVIRONMENT = os.getenv('ENV', 'dev')  # default: dev

ENVIRONMENTS = {
    "dev": {
        "url": "https://dev.your-app-url.com",
        "username": "dev-user@example.com",
        "password": "dev-password"
    },
    "staging": {
        "url": "https://staging.your-app-url.com",
        "username": "staging-user@example.com",
        "password": "staging-password"
    },
    "prod": {
        "url": "https://your-app-url.com",
        "username": "prod-user@example.com",
        "password": "prod-password"
    }
}

# Get current environment config
BASE_URL = ENVIRONMENTS[ENVIRONMENT]["url"]
USERNAME = ENVIRONMENTS[ENVIRONMENT]["username"]
PASSWORD = ENVIRONMENTS[ENVIRONMENT]["password"]

# Tambahkan konfigurasi lain yang bisa digunakan di banyak tes
TIMEOUT = 10
IMPLICIT_WAIT = 10

# Screenshot Configuration
SCREENSHOT_ON_FAILURE = True
SCREENSHOT_PATH = "artifacts/screenshots"
