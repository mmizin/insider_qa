import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from ui_tests.config import BASE_URL


@pytest.fixture(autouse=True)
def close_cookie_banner(fxt_webdriver):
    if not fxt_webdriver.current_url or fxt_webdriver.current_url.startswith("data:"):
        fxt_webdriver.get(BASE_URL)
        
    try:
        accept_button = WebDriverWait(fxt_webdriver, 3).until(
            EC.element_to_be_clickable((By.ID, "wt-cli-accept-all-btn"))
        )
        accept_button.click()
    except TimeoutException:
        pass
