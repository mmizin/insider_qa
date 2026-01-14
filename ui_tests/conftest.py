import pytest
import os
from datetime import datetime
from ui_tests.config import BrowserTypes

DEFAULT_BROWSERS = [browser.value for browser in BrowserTypes]

pytest_plugins = [
    "ui_tests.fixtures.fxt_webdriver",
]


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default=None,
        help=f"Browser to run tests: {DEFAULT_BROWSERS}"
    )
    
    parser.addoption(
        "--headless",
        action="store_true",
        help="Run browser in headless mode"
    )


def pytest_generate_tests(metafunc):
    """Dynamically parametrize tests with browsers, only if the fixture is present"""
    
    if "fxt_webdriver" in metafunc.fixturenames:
        browser_cli = metafunc.config.getoption("--browser")
        browsers = [browser_cli.lower()] if browser_cli else DEFAULT_BROWSERS
        metafunc.parametrize("browser_name", browsers)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Take screenshot on test failure."""
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        driver = None
        
        if "fxt_webdriver" in item.funcargs:
            driver = item.funcargs["fxt_webdriver"]
        elif hasattr(item.cls, "driver"):
            driver = getattr(item.cls, "driver", None)
        
        if driver:
            try:
                screenshots_dir = os.path.join(os.getcwd(), "screenshots")
                os.makedirs(screenshots_dir, exist_ok=True)
                
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                test_name = item.nodeid.replace("::", "_").replace("/", "_")
                path = os.path.join(screenshots_dir, f"{test_name}_{timestamp}.png")
                
                driver.save_screenshot(path)
                
                print(f"\nSaved screenshot: {path}")
            except Exception as e:
                print(f"Failed to capture screenshot: {e}")
        else:
            print("No webdriver instance found for screenshot.")
