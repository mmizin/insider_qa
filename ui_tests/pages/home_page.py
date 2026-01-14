from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from ui_tests.pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    NAVIGATION = (By.CSS_SELECTOR, "#navigation")
    
    def open(self):
        self.open_url()
    
    def is_loaded(self) -> bool:
        try:
            self.wait_for_element(self.NAVIGATION)
            return True
        except TimeoutException:
            return False