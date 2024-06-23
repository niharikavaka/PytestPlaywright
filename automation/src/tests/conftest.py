import pytest
from src.resources import locators


@pytest.fixture()
def set_up_tear_down(page):
     page.goto('https://practice.expandtesting.com/')
     page.locator(locators.Login.DROPDOWN).click()
     page.locator(locators.Login.EXAMPLES).click()
     yield page



