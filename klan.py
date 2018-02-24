## class for work with help windowz1

import pyautogui
from commons import find_and_click, close_window, move_to_center

def open_clan():
    ''' open klan window'''
    pyautogui.press('c')

def click_help():
    ''' click help for all klan mates'''
    open_clan()

    if find_and_click('data/klan_help.png'):
        # click on 'help all' button
        find_and_click('data/b_help.png')  # returns (x, y) of matching region

    # close all windows
    while close_window():
        move_to_center()


if __name__ == "__main__":
    from commons import test

    test(click_help)