# 🌎 UI Tests – Selenium + Pytest 🐍

UI automation framework for testing Insider / InsiderOne web application using
Python, Selenium, Pytest and Page Object Model (POM).

---

## 📁 Project Structure

```text
ui_tests/
├── config.py                # Global configuration (BASE_URL, timeouts, etc.)
├── conftest.py              # Pytest configuration & hooks
│
├── fixtures/                # Pytest fixtures
│   ├── fxt_webdriver.py     # WebDriver setup (browser, headless, teardown)
│   └── fxt_cookie.py        # Auto-handling cookie banner
│
├── pages/                   # Page Object Model
│   ├── base_page.py
│   ├── home_page.py
│   ├── careers_page.py
│   ├── career_roles_page.py
│   └── careers_open_positions_page.py
│
├── tests/                   # UI tests
│   ├── test_home_page.py
│   ├── test_careers_page.py
│   └── test_browse_open_positions.py
│
└── utils/                   # Shared helpers (future extensions)
```


## 🧠 Architecture

- Page Object Model (POM)
- Selenium WebDriver
- Pytest fixtures for setup/teardown
- No test logic inside page objects
- Auto-handling of cookie banner
- Screenshot on test failure

---

## ⚙️ Requirements

- Python 3.11+
- Google Chrome or Firefox
- pip

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🧠 Architecture

- Page Object Model (POM)
- Selenium WebDriver
- Pytest fixtures for setup/teardown
- No test logic inside page objects
- Auto-handling of cookie banner
- Screenshot on test failure

---

## ⚙️ Requirements

- Python 3.11+
- Google Chrome or Firefox
- pip

## Install dependencies:

```bash
pip install -r requirements.txt
```

## 🧪 Test Execution & Parallel Runs
This project uses pytest-xdist to run UI tests in parallel, 
which helps reduce execution time and improve feedback speed.

### Run tests in parallel

Run tests using multiple workers for default browsers(Chrome, Firefox):
```bash
pytest -n auto -m UI
```
or specify the exact number of workers:
```bash
pytest -n 4 -m UI
```
### Notes on parallel execution
- Each test runs with its own WebDriver instance
- Browser sessions are fully isolated
- Fixtures are designed to be xdist-safe
- Parallel execution is optional — tests can be run sequentially without changes

---

### Example run command (recommended)
```bash
pytest -m UI -n auto --browser=chrome --headless
```

---

## 🌍 Browser Options
```aiignore
pytest -m UI --browser=chrome
pytest -m UI --browser=firefox
pytest -m UI --headless
```

Defaults:
Browser: Chrome Firefox
Headless: disabled

## 🏷️ Pytest Markers
```aiignore
@pytest.mark.UI — UI tests
```
Example:
@pytest.mark.UI
```python
def test_home_page():
    ...
```

## 🍪 Cookie Banner

Cookie consent banner is closed automatically using an autouse fixture:
Opens BASE_URL if browser starts on data:
Clicks Accept All if banner is present
Ignored if banner does not exist
No cookie handling required in tests.

## 📸 Screenshots on Failure

Screenshot is taken automatically if a test fails
Saved locally for debugging
Useful for CI and local runs