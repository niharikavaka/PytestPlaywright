from src.pages.radio_button.RadioButton import RadioButton
from playwright.sync_api import expect
import pytest 
import random

from src.data.data1 import Data


@pytest.mark.parametrize("colors,sports",Data.color_sport_list)
def xtest_radio_button_check(set_up_tear_down,colors,sports):
    page=set_up_tear_down
    # input={'color':'yellow','sport':'Football'}
    # radio_button = RadioButton(page)
    # success=radio_button.do_check(input)
    # expect(success['color']).to_be_checked()
    # expect(success['sport']).to_be_checked()
    radio_button = RadioButton(page)
    success = radio_button.do_check(colors,sports)

    expect(success['color']).to_be_checked()
    expect(success['sport']).to_be_checked()


