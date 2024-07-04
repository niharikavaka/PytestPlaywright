import pytest
from src.pages.forgot.ForgotPage import ForgotPage
from playwright.sync_api import expect

from src.data.data1 import Data

# @pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])


@pytest.mark.parametrize('email', Data.forgot_email_list)
def test_forgot_email(set_up_tear_down, email):
    page = set_up_tear_down
    forgot_page = ForgotPage(page)
    success = forgot_page.do_retrieve_password(email)
    expect(success).to_have_text(
        'An e-mail has been sent to you which explains how to reset your password.')


def test_forgot_email_with_no_credentials(set_up_tear_down):
    page = set_up_tear_down
    forgot_page = ForgotPage(page)
    no_cred = forgot_page.err_no_email()
    expect(no_cred).to_have_text('Please enter a valid email address.')
