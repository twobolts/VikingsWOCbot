## class for work with help windowz1

import pyautogui
from commons import find_and_click, close_window

def run():
    # click on help button
    res = find_and_click('data/l_help.png')

    if res:
        # click on 'help all' button
        find_and_click('data/b_help.png')  # returns (x, y) of matching region
        close_window()