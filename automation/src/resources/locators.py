class Login:
    DROPDOWN = "[id='examples-dropdown']"
    EXAMPLES = 'a:text-is("Examples")'
    LOGINFORM = 'a:text-is("Login Form")'
    USERNAME = '[id="username"]'
    PASSWORD = '[id="password"]'
    LOGINBUTTON = 'button[type="submit"]'

class Forgot:
    FORGOTFORM = 'a:text-is("Forgot Password Form")'
    FORGOTEMAIL= "[id='email']"
    RETRIEVEPASSWORD = 'button[type="submit"]'

class RadioButton:
    RADIOBUTTONFORM = 'a:text-is("Radio Buttons")'
    COLOR = '[id="{}"]'
    SPORT = '[id="{}"]'
    


