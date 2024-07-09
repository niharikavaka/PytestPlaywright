import pytest
from automation.src.resources.locators import Login


@pytest.fixture()
def set_up_tear_down(page):
    page.goto('https://practice.expandtesting.com/')
    page.locator(Login.DROPDOWN).click()
    page.locator(Login.EXAMPLES).click()
    yield page
