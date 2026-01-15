# 🔥🐞 Test Automation Project – UI & API 🐞🔥

This repository contains automated test suites for **UI** and **API** testing, implemented in Python using **Selenium** for UI and **requests** for API.  

---

## ✍️ Manual Testing Scenarios Analysis

1. **Pencil with Eraser Testing**  
   Full functional, usability, performance, load, stress, and security testing scenarios.  
   [View analysis document](https://github.com/mmizin/insider_qa/blob/master/pencil_with_eraser_qa_test_coverage.md)

2. **Hepsiburada Product Recommendations Analysis**  
   Study of Recommendations sections across Main, Product Detail, and Cart pages.  
   [View analysis document](https://github.com/mmizin/insider_qa/blob/master/page_recommendations_analysis.md)

---

## 💻🌎 UI Test Automation

- Framework: **Python + Pytest + Selenium**
- Page Object Model fully implemented
- Cross-browser support: Chrome & Firefox
- Screenshots captured automatically on failures
- Parallel execution supported via **xdist**

---

## 💻 👷 API Test Automation

- Framework: **Python + Pytest + Requests**
- CRUD operations for `Pet` endpoints ([Swagger Petstore](https://petstore.swagger.io/))
- Positive and negative test scenarios
- In-memory image upload using `io.BytesIO`
- Parallel execution supported via **xdist**

---

## 🌳 Project Structure

```text
ui_tests/ and api_tests/ combined structure:

UI Testing
├── ui_tests/
│ ├── config.py # Global configuration (BASE_URL, timeouts)
│ ├── conftest.py # Pytest hooks and global fixtures
│ ├── fixtures/ # Pytest fixtures
│ │ ├── fxt_webdriver.py
│ │ └── fxt_cookie.py
│ ├── pages/ # POM classes
│ │ ├── base_page.py
│ │ ├── home_page.py
│ │ ├── careers_page.py
│ │ ├── career_roles_page.py
│ │ └── careers_open_positions_page.py
│ ├── tests/ # Test cases
│ │ ├── test_home_page.py
│ │ ├── test_careers_page.py
│ │ └── test_browse_open_positions.py
│ └── utils/ # Helpers (e.g., screenshot)
│ └── generate_screenshot.py

API Testing
├── api_tests/
│ ├── api/
│ │ ├── base_api.py
│ │ ├── config.py
│ │ └── pet_api.py
│ ├── fixtures/
│ │ ├── fxt_pet_api.py
│ │ └── fxt_add_pet.py
│ ├── tests/
│ │ ├── test_create_pets.py
│ │ ├── test_delete_pets.py
│ │ ├── test_get_pets.py
│ │ ├── test_update_pets.py
│ │ └── test_image_upload_pet.py
│ └── utils/
│ ├── api_payloads.py
│ ├── enums.py
│ └── generate_image_file.py
```


---

## 🔑 Key Features

- **UI Tests**
  - Full POM implementation
  - Cross-browser (Chrome/Firefox)
  - Screenshots captured on failure
  - Parameterized tests and fixtures
  - Auto-handling cookie banners
  - Parallel execution via `pytest-xdist`

- **API Tests**
  - Full CRUD coverage
  - Positive and negative test scenarios
  - Image upload support (in-memory)
  - Payload builders & enumerations
  -   - Parallel execution via `pytest-xdist`

- **General**
  - Independent, reusable fixtures
  - Easy parametrization
  - Supports both UI and API test execution in parallel

---

## 🧑‍💻 Running Tests

**Install dependencies:**

```bash
pip install -r requirements.txt
```
Run all UI tests:
```bash
pytest ui_tests/ -n auto -v
```


Run all API tests:
```bash
pytest api_tests/ -n auto -v
```


Run specific test file:
```bash
pytest ui_tests/tests/test_careers_page.py -v
```


Run tests by marker:
```bash
pytest -m "API and CREATE_PET" -v
```

### 🤘 Notes

- Uses requests library for API calls.
- Image upload uses in-memory files via io.BytesIO.
- Screenshots are generated automatically on test failure.
- All tests are independent and use fixtures for setup/teardown.
- Enumerations (enums.py) and payload builders (api_payloads.py) help maintain consistency across tests.