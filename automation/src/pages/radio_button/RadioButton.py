
from src.pages.radio_button import locators


class RadioButton:
    def __init__(self,page):
        self.page = page
        self.radio_button_form=page.locator(locators.RadioButton.RADIOBUTTONFORM)
        # self.sport = page.locator(locators.RadioButton.SPORT)

    def check_color(self,color):
        self.color = self.page.locator(locators.RadioButton.COLOR.format(color))
        self.color.check() 
 
    def check_sport(self,sport):
        self.sport = self.page.locator(locators.RadioButton.SPORT.format(sport))
        self.sport.check()

    def do_check(self,color,sport):
        self.radio_button_form.click()
        self.check_color(color)
        self.check_sport(sport)

        return {'color':self.color,'sport' : self.sport }
        # self.check_color(input['color'])
        # self.check_sport(input['sport'])
        # return {'color':self.yellow_color, 'sport': self.football_sport}
          

        