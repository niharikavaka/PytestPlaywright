from src.pages.forgot import locators


class ForgotPage:
    def __init__(self, page):
        self.page = page
        self.forgot_form = page.locator(locators.Forgot.FORGOTFORM)
        self.email = page.locator(locators.Forgot.FORGOTEMAIL)
        self.retrieve_btn = page.locator(locators.Forgot.RETRIEVEPASSWORD)

    def enter_email(self, email):
        self.email.fill(email)

    def click_retrieve(self):
        self.retrieve_btn.click()

    def do_retrieve_password(self, input_email):
        self.forgot_form.click()
        self.enter_email(input_email)
        self.click_retrieve()

        return self.page.locator('[id="confirmation-alert"]')

    def err_no_email(self):
        self.forgot_form.click()
        self.click_retrieve()
        return self.page.locator('div:text-is("Please enter a valid email address.")')
