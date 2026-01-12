from typing import Optional, NoReturn

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ui_tests.config import EXPLICIT_WAIT, BASE_URL


class BasePage:
    def __init__(self, driver, timeout=EXPLICIT_WAIT):
        self.driver = driver
        self.timeout = timeout
        self.base_url = BASE_URL
    
    def open_url(self, url: Optional[str] = "") -> NoReturn:
        full_url = f"{self.base_url.rstrip('/')}/{url.lstrip('/')}"
        self.driver.get(full_url)
    
    def wait_for_element(self, by_locator: tuple[By, str]) -> WebElement:
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(by_locator)
        )
    
    def find_element(self, by_locator: tuple[By, str]):
        return self.wait_for_element(by_locator)
