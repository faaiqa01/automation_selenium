import pytest
from pathlib import Path
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from config import BASE_URL, USERNAME, PASSWORD, SCREENSHOT_ON_FAILURE, SCREENSHOT_PATH
from utils.logger import CustomLogger

# --- Global Config ---
VIDEO_PATH = Path(__file__).parent / "artifacts/videos"
SCREENSHOT_DIR = Path(__file__).parent / SCREENSHOT_PATH

# --- Setup Global Logger ---
logger = CustomLogger.get_logger("TestExecution")

# --- Basic Setup Fixtures ---

@pytest.fixture(scope="function")
def driver(request):
    """Fixture to set up and tear down WebDriver."""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    
    yield driver
    
    # Teardown
    driver.quit()

@pytest.fixture(scope="function")
def logged_in_driver(driver):
    """Handles the login process, provides logged-in driver."""
    session_file_path = Path(__file__).parent / "session.json"
    
    try:
        # Try login with saved cookies
        driver.get(BASE_URL)
        with open(session_file_path, "r") as f:
            cookies = json.load(f)
        for cookie in cookies:
            driver.add_cookie(cookie)
        
        logger.info("Cookie ditemukan, mencoba memuat sesi...")
        driver.get(BASE_URL + "/dashboard")  # Adjust to your app's landing page
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "sidebar")))  # Adjust selector
        logger.info("Login via cookie berhasil!")
        
    except Exception as e:
        # If cookie login fails, do UI login
        logger.warning(f"Gagal login via cookie. Melakukan login via UI... ({e})")
        driver.get(BASE_URL)
        
        # CUSTOMIZE THIS SECTION BASED ON YOUR LOGIN PAGE
        login_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
        )
        login_link.click()
        
        username_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        password_field = driver.find_element(By.NAME, "password")
        
        username_field.clear()
        username_field.send_keys(USERNAME)
        password_field.clear()
        password_field.send_keys(PASSWORD)
        time.sleep(1)
        
        sign_in_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "login-button"))
        )
        sign_in_button.click()
        
        WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL + "/dashboard"))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "sidebar")))
        
        logger.info("Login via UI berhasil.")
        
        # Save cookies for next time
        with open(session_file_path, "w") as f:
            json.dump(driver.get_cookies(), f)
        logger.info("Cookie baru telah disimpan.")
    
    yield driver

# --- Hooks for HTML Report ---

def pytest_configure(config):
    """Auto-generate HTML report with timestamp."""
    if not config.option.htmlpath:
        reports_dir = Path('reports')
        reports_dir.mkdir(exist_ok=True)
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        test_paths = config.getoption('file_or_dir')
        base_name = f"report_{timestamp}"
        if test_paths and len(test_paths) == 1 and ".py" in test_paths[0]:
            base_name = Path(test_paths[0]).stem
        config.option.htmlpath = str(reports_dir / f"{base_name}.html")
        config.option.self_contained_html = True

import pytest_html

def pytest_html_results_table_row(report, cells):
    """Add captured logs to HTML report."""
    if report.passed or report.failed or report.skipped:
        log_content = ""
        for section in report.sections:
            if section[0] == 'Captured stdout':
                log_content += f"--- Captured Stdout ---\n{section[1]}\n"
            elif section[0] == 'Captured stderr':
                log_content += f"--- Captured Stderr ---\n{section[1]}\n"
        if log_content:
            cells.insert(2, pytest_html.extras.html(f"<pre>{log_content}</pre>"))

# --- Screenshot on Failure ---

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Take screenshot on test failure."""
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == 'call' and rep.failed and SCREENSHOT_ON_FAILURE:
        # Get driver from test fixtures
        driver = None
        if 'driver' in item.funcargs:
            driver = item.funcargs['driver']
        elif 'logged_in_driver' in item.funcargs:
            driver = item.funcargs['logged_in_driver']
        
        if driver:
            # Create screenshot directory
            SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
            
            # Generate screenshot filename
            timestamp = time.strftime('%Y%m%d_%H%M%S')
            test_name = item.name
            screenshot_name = f"{test_name}_{timestamp}.png"
            screenshot_path = SCREENSHOT_DIR / screenshot_name
            
            # Take screenshot
            try:
                driver.save_screenshot(str(screenshot_path))
                logger.info(f"📸 Screenshot saved: {screenshot_path}")
                
                # Add screenshot to HTML report
                if hasattr(rep, 'extra'):
                    extra = getattr(rep, 'extra', [])
                    extra.append(pytest_html.extras.image(str(screenshot_path)))
                    rep.extra = extra
            except Exception as e:
                logger.error(f"❌ Failed to take screenshot: {e}")
