from automation.src.pages.login import locators


class LoginPage:

    def __init__(self, page):
        self.page = page
        self.login_form = page.locator(locators.Login.LOGINFORM)
        self.username = page.locator(locators.Login.USERNAME)
        self.password = page.locator(locators.Login.PASSWORD)
        self.login_button = page.locator(locators.Login.LOGINBUTTON)

    def enter_username(self, username):
        self.username.fill(username)

    def enter_password(self, password):
        self.password.fill(password)

    def click_login(self):
        self.login_button.click()

    def do_login(self, credentials):
        self.login_form.click()
        self.enter_username(credentials['username'])
        self.enter_password(credentials['password'])
        self.click_login()
        return self.page.locator("[id='flash']")
