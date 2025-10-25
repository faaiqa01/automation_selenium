# Selenium Automation Testing Project

Project automation testing menggunakan Selenium WebDriver dan Pytest.

## Prerequisites
- Python 3.8+
- Google Chrome Browser
- ChromeDriver (auto-managed by Selenium Manager)

## Installation

1. Clone repository
```bash
git clone <your-repo-url>
cd <project-folder>
```

2. Create virtual environment
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure credentials
Edit `config.py` and update environment settings:
- ENVIRONMENTS (dev/staging/prod)
- Update BASE_URL, USERNAME, PASSWORD for each environment

## Running Tests

Run all tests:
```bash
pytest -s --html=reports/report.html
```

Run specific test file:
```bash
pytest -s tests/test_example.py --html=reports/test_example.html
```

Run specific test case:
```bash
pytest -s tests/test_example.py::test_example_navigation
```

Run tests by marker:
```bash
pytest -s -m example_suite
```

Run tests with specific environment:
```bash
# Windows
set ENV=staging && pytest -s

# Linux/Mac
ENV=staging pytest -s
```

## Project Structure
```
project_root/
├── Pages/           # Page Object Models
├── tests/           # Test cases
├── utils/           # Helper utilities
├── reports/         # HTML reports
├── conftest.py      # Pytest fixtures
├── config.py        # Configuration
└── pytest.ini       # Pytest settings
```

## Features
- Auto-login with session cookies
- HTML test reports with screenshots on failure
- Multi-environment support (dev/staging/prod)
- Modular fixture design with Page Object Model
- Test data management
- Screenshot on test failure
- Custom wait helpers for complex scenarios
- Professional logging system with file & console output
- Easy configuration management

## Tips & Best Practices
1. SELALU gunakan fixture logged_in_driver untuk test yang membutuhkan login
2. GUNAKAN markers untuk mengelompokkan test cases
3. TAMBAHKAN print statements untuk debugging di output console
4. GUNAKAN WebDriverWait untuk menunggu elemen, hindari time.sleep()
5. SIMPAN kredensial sensitif di environment variables (production)
6. BUAT Page Object Model untuk halaman yang kompleks
7. JALANKAN test dengan flag -s untuk melihat output print
8. REVIEW HTML report di folder reports/ setelah test selesai
