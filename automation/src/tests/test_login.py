from playwright.sync_api import Page
from playwright.sync_api import expect
from src.resources import locators
from src.pages.login.LoginPage import LoginPage

import pytest
from src.data.data1 import Data

@pytest.mark.usefixtures("set_up_tear_down")
class TestLogin:
    
    def test_login_with_standard_input(self,set_up_tear_down):
        page=set_up_tear_down
        credentials=Data.user_data                             
        login_page=LoginPage(page)
        success=login_page.do_login(credentials)
        expect(success).to_have_text("You logged into a secure area!")
 
    def xtest_login_with_invalid_user(self,set_up_tear_down):
        page=set_up_tear_down
        credentials=Data.invalid_user_data
        login_page=LoginPage(page)
        fail=login_page.do_login(credentials)
        if credentials['username'] != "practice":
            expect(fail).to_have_text("Your username is invalid!")
        else:
            expect(fail).to_have_text("Your password is invalid!")
 
