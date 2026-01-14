import time

from typing import Optional
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from ui_tests.pages.base_page import BasePage


class CareersOpenPositionsPage(BasePage):
    URL = "/careers/open-positions"
    REDIRECT_TO_LEVER_URL = "https://jobs.lever.co/insiderone/"
    
    TITLE = (By.XPATH, "//h3[normalize-space()='Browse Open Positions']")
    
    NO_POSITIONS_AVAILABLE = (By.XPATH, "//p[normalize-space()='No positions available']")
    JOBS_LIST = (By.CSS_SELECTOR, "#jobs-list .position-list-item")
    
    FILTER_BY_DEPARTMENT = (By.CSS_SELECTOR, "#filter-by-department")
    FILTER_BY_LOCATION = (By.CSS_SELECTOR, "#filter-by-location")
    
    VIEW_ROLE_BUTTON = (By.CSS_SELECTOR, "a.btn.btn-navy.rounded[target='_blank']")
    
    def __init__(self,
                 driver,
                 url_params: dict,
                 department: Optional[tuple] = None,
                 location: Optional[tuple] = None,
                 
                 ):
        super().__init__(driver)
        self.department = department
        self.location = location
        self.url_params = url_params
    
    def open(self):
        url = self.URL
        if self.url_params:
            if self.url_params["department"]:
                url += f"{'?department=' + self.url_params["department"]}"
                if self.url_params["location"]:
                    url += f"{'&location=' + self.url_params["location"]}"
        elif self.url_params["location"]:
            url += f"?location={self.url_params["location"]}"
        
        self.open_url(url)
    
    def is_loaded(self) -> bool:
        try:
            self.wait_for_element(self.TITLE)
            return True
        except TimeoutException:
            return False
    
    def wait_for_positions_loaded(self):
        try:
            self.wait_for_element(self.JOBS_LIST)
            time.sleep(2)
        except TimeoutException:
            try:
                self.wait_for_element(self.NO_POSITIONS_AVAILABLE)
                time.sleep(2)
            except TimeoutException:
                pass
        
    def select_department(self):
        self.wait_for_positions_loaded()
        
        select = Select(self.find_element(self.FILTER_BY_DEPARTMENT))
        for option in select.options:
            if self.department[1] in (option.get_attribute("class") or ""):
                option.click()
                return
        raise AssertionError(f"Department/team with code '{self.department[1]}' not found")
    
    def select_location(self):
        select = Select(self.find_element(self.FILTER_BY_LOCATION))
        for option in select.options:
            if self.location[1] in (option.get_attribute("class") or ""):
                option.click()
                self.wait_for_positions_loaded()
                return
        raise AssertionError(f"Location with code '{self.location[1]}' not found")
    
    def apply_filters(self):
        if self.department:
            self.select_department()
        if self.location:
            self.select_location()
    
    def check_positions_available(self) -> bool:
        try:
            return self.find_elements(self.JOBS_LIST)
        except TimeoutException:
            return False
        
    def check_positions_attributes(self, positions: list[WebElement]) -> bool:
        try:
            for position in positions:
                assert position.get_attribute("data-location") == self.location[1]
                assert position.get_attribute("data-team") == self.department[1]
            return True
        except AssertionError:
            return False
    
    def click_view_role(self, position: WebElement):
        position.find_element(*self.VIEW_ROLE_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
    
    def is_redirected_to_lever(self):
        return self.REDIRECT_TO_LEVER_URL in self.driver.current_url
    
    def my_sleep(self):
        time.sleep(3)

