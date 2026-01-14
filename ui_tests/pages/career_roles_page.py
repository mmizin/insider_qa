from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from ui_tests.pages.base_page import BasePage


class CareerRolesPage(BasePage):
    URL = "/careers/"
    
    TITLE = (By.CSS_SELECTOR, "h1.big-title.big-title-media")
    SEE_ALL_JOBS_BTN = (By.CSS_SELECTOR, "div.button-group a.btn[href*='open-positions']")
    
    def __init__(self, driver, slug):
        super().__init__(driver)
        self.slug = slug
    
    def open(self):
        url = f"/{self.URL}/{self.slug}/"
        self.open_url(url)
    
    def is_loaded(self) -> bool:
        try:
            self.wait_for_element(self.TITLE)
            return True
        except TimeoutException:
            return False
    
    def click_see_all_jobs_btn(self):
        self.click(self.SEE_ALL_JOBS_BTN)
