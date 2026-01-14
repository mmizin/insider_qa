import pytest

from ui_tests.pages.careers_page import CareersPage

SCENARIOS = [
    ("Life at Insider One", CareersPage.LIFE_AT_INSIDER, CareersPage.FIRST_LIFE_AT_INSIDER_SLIDE),
    ("Teams", CareersPage.TEAMS, CareersPage.FIRST_TEAM),
    ("Locations", CareersPage.LOCATIONS, CareersPage.FIRST_LOCATION),
]

@pytest.mark.UI
@pytest.mark.parametrize("name, section_locator, first_item_locator", SCENARIOS)
def test_careers_page_sections_present(fxt_webdriver, name, section_locator, first_item_locator):
    page = CareersPage(fxt_webdriver)
    page.open(page.URL)
    
    assert page.is_loaded(), "Careers page did not load correctly"
    
    assert page.is_section_present(section_locator), f"{name} section is not present"
    assert page.is_first_element_visible(first_item_locator), f"First slide in {name} block is not visible or active"
