## common functions

import ocv
import pyautogui

def find_and_click(img):
    ''' find the element on the screen and click on it
        :returns
            True if element was found'''
    b_location = ocv.locateCenterOnScreen(img)
    if b_location:
        pyautogui.click(b_location[0], b_location[1])  # close message
        return True

def close_window():
    ''' try to find close button "X" and click it
        :returns
            True - if button was found
            False - if button wasn't found
        '''
    return find_and_click('data/b_x.png')