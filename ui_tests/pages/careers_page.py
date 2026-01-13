from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from ui_tests.pages.base_page import BasePage


class CareersPage(BasePage):
    URL = "/careers/"
    
    # Sections headers
    EXPLORE_OPEN_ROLES = (By.XPATH, "//a[.//span[normalize-space()='Explore open roles']]")
    LIFE_AT_INSIDER = (By.XPATH, "//h2[normalize-space()='Life at Insider One']")
    LOCATIONS = (By.XPATH, "//h2[normalize-space()='Our locations' or normalize-space()='Locations']")
    TEAMS = (By.CSS_SELECTOR, ".insiderone-icon-cards-grid.columns-3")
    
    FIRST_LOCATION = (By.CSS_SELECTOR,
                      ".insiderone-locations-slider-slides .swiper-slide:first-child")
    FIRST_TEAM = (By.CSS_SELECTOR, ".insiderone-icon-cards-grid.columns-3 > div:first-child")
    FIRST_LIFE_AT_INSIDER_SLIDE = (By.CSS_SELECTOR, ".insiderone-gallery-slider-slides .swiper-slide:first-child")

    def is_loaded(self) -> bool:
        try:
            self.wait_for_element(self.EXPLORE_OPEN_ROLES)
            return True
        except TimeoutException:
            return False
    
    # Generic section presence check
    def is_section_present(self, locator) -> bool:
        try:
            self.scroll_to_element(locator)
            self.wait_for_element(locator)
            return True
        except TimeoutException:
            return False
    
    def scroll_to_element(self, locator):
        """Scroll page until element is in view"""
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return element
    
   
    
    # First slide in Life at Insider block
    def is_first_element_visible(self, locator) -> bool:
        first_elem = self.driver.find_element(*locator)
        return first_elem.is_displayed()
 