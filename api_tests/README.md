# 💻 API Test Automation – PetStore 🐍

This project contains automated API tests for the [PetStore Swagger API](https://petstore.swagger.io/).

---

## 📁 Project Structure

```text
api_tests/
├── api/ # API layer (BaseApi + specific endpoints)
│ ├── base_api.py # Base API client with common methods (GET, POST, PUT, DELETE)
│ ├── config.py # API configuration (BASE_URL, headers, etc.)
│ └── pet_api.py # Pet-specific API actions (CRUD, image upload)
│
├── fixtures/ # Pytest fixtures
│ ├── fxt_pet_api.py # PetApi instance fixture
│ └── fxt_add_pet.py # Fixture to create a pet before tests
│
├── tests/ # API test cases
│ ├── test_create_pets.py # Create pet positive/negative scenarios
│ ├── test_delete_pets.py # Delete pet scenarios
│ ├── test_get_pets.py # Get pet scenarios
│ ├── test_update_pets.py # Update pet scenarios
│ └── test_image_upload_pet.py # Upload pet image scenarios
│
├── utils/ # Shared helpers
│ ├── api_payloads.py # Payload builders for API requests
│ ├── enums.py # Enumerations (status, types, etc.)
│ └── generate_image_file.py # Helper to generate in-memory images
│
├── conftest.py # Pytest configuration
└── init.py
```

---

## 👷  Test Features

- **CRUD operations for pets**
  - Create, Read, Update, Delete
  - Positive and negative test scenarios
- **Image upload testing**
  - Supports JPEG and PNG
  - Negative tests for invalid file types
- **Parameterized tests**
  - Using `pytest.mark.parametrize` for different scenarios
- **Fixtures**
  - `fxt_pet_api` for API client
  - `fxt_add_pet` to create reusable pets for tests

---

## 🧪 Running Tests

Install dependencies:

```bash
pip install -r requirements.txt
```

Run all tests:
```bash
pytest -v
```

Run specific test file:
```bash
pytest tests/test_create_pets.py -v
```

Run tests in parallel (using pytest-xdist):
```bash
pytest -n auto -v
```

Run tests with markers:
```bash
pytest -m "API and CREATE_PET" -v
```
---
### 🤘 Notes
- Uses requests library for HTTP calls.
- Image upload uses in-memory files via io.BytesIO.
- All tests are independent and use fixtures for setup/teardown.
- Enumerations (enums.py) and payload builders (api_payloads.py) help maintain consistency across tests.