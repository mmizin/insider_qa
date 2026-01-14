import random

import pytest

from ui_tests.pages.career_roles_page import CareerRolesPage
from ui_tests.pages.careers_open_positions_page import CareersOpenPositionsPage

SCENARIOS = [
    (
        "quality-assurance",
        ("Quality Assurance", "qualityassurance"),
        ("Istanbul, Turkiye", "istanbulturkiye"),
        {"department": "qualityassurance", "location": False}
    ),
]


@pytest.mark.UI
@pytest.mark.parametrize("slug, department, location, url_params", SCENARIOS)
def test_browse_open_propositions(fxt_webdriver, slug, department, location, url_params):
    career_role_page = CareerRolesPage(fxt_webdriver, slug)
    careers_open_position_page = CareersOpenPositionsPage(
        driver=fxt_webdriver,
        department=department,
        location=location, url_params=url_params)
    
    career_role_page.open()
    career_role_page.is_loaded()
    career_role_page.click_see_all_jobs_btn()
    
    careers_open_position_page.is_loaded()
    careers_open_position_page.apply_filters()
    
    propositions = careers_open_position_page.check_positions_available()
    assert propositions, "No positions available"
    assert careers_open_position_page.check_positions_attributes(
        propositions), "Positions attributes: location/department are not correct"
    
    careers_open_position_page.click_view_role(random.choice(propositions))
    assert careers_open_position_page.is_redirected_to_lever()