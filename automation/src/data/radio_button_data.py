import random
class RadioButtondata:
    strings = ["basketball","football","tennis"]
    random_string = random.choice(strings)
    color_sport_list = [('yellow',random_string),('blue',random_string),
                        ('red',random_string),('black',random_string),('green',random_string)]