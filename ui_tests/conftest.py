import pytest
from selenium import webdriver
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
