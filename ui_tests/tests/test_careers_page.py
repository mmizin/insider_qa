import pytest

from ui_tests.pages.careers_page import CareersPage


@pytest.mark.UI
@pytest.mark.MYTEST
def test_careers_page_sections_present(fxt_webdriver):
    careers = CareersPage(fxt_webdriver)
    careers.open_url(careers.URL)
    
    assert careers.is_loaded(), "Careers page did not load correctly"
    
    assert careers.is_life_at_insider_present(), "Life at Insider One section is not present"
    assert careers.is_first_life_at_insider_slide_visible(), "First slide in Life at Insider block is not visible or active"
    
    assert careers.is_teams_present(), "Teams section is not present"
    assert careers.is_first_team_visible(), "First Team not visible"
    
    assert careers.is_locations_present(), "Locations section is not present"
    assert careers.is_first_location_visible(), "First Location not visible"

    

    

    
