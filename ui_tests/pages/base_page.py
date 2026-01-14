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
    
    def wait_for_element(self, by_locator: tuple[By, str], timeout: Optional[int] = 0) -> WebElement:
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.presence_of_element_located(by_locator)
        )
    
    def wait_for_elements(self, by_locator: tuple[By, str], timeout: Optional[int] = 0) -> WebElement:
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.presence_of_all_elements_located(by_locator)
        )
    
    def find_element(self, by_locator: tuple[By, str]):
        return self.wait_for_element(by_locator)
    
    def find_elements(self, by_locator: tuple[By, str]):
        return self.wait_for_elements(by_locator)
    
    def scroll_to_element(self, locator):
        """Scroll page until element is in view"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return element
    
    def click(self, locator):
        element = self.wait_for_element(locator)
        self.scroll_to_element(locator)
        element.click()
