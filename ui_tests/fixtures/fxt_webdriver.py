import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from ui_tests.config import BrowserTypes


@pytest.fixture()
def fxt_webdriver(browser_name, request):
    headless = request.config.getoption("--headless")
    
    if browser_name == BrowserTypes.CHROME.value:
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
        
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    
    elif browser_name == BrowserTypes.FIREFOX.value:
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
    
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    
    driver.maximize_window()
    yield driver
    driver.quit()
