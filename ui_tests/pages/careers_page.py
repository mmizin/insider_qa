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
    
    # Section presence methods
    def is_life_at_insider_present(self):
        return self.is_section_present(self.LIFE_AT_INSIDER)
    
    def is_locations_present(self):
        return self.is_section_present(self.LOCATIONS)
    
    def is_teams_present(self):
        return self.is_section_present(self.TEAMS)
    
    # First slide in Life at Insider block
    def is_first_life_at_insider_slide_visible(self) -> bool:
        first_slide = self.driver.find_element(*self.FIRST_LIFE_AT_INSIDER_SLIDE)
        img = first_slide.find_element(By.TAG_NAME, "img")
        return img.is_displayed()
    
    # First location visible
    def is_first_location_visible(self) -> bool:
        first_location = self.driver.find_element(*self.FIRST_LOCATION)
        return first_location.is_displayed()
    
    # First team visible
    def is_first_team_visible(self) -> bool:
        first_team = self.driver.find_element(*self.FIRST_TEAM)
        return first_team.is_displayed()
