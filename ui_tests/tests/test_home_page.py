import pytest
from ui_tests.pages.home_page import HomePage


@pytest.mark.UI
def test_insider_home_page(fxt_webdriver):
    """Visit Insider home page and verify it is opened"""
    page = HomePage(fxt_webdriver)
    page.open()
    
    assert page.is_loaded(), "Insider home page did not load correctly"
