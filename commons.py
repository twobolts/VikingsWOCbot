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
    b_close_location = ocv.locateOnScreen('data/b_x.png')

    if b_close_location:
        buttonx, buttony = pyautogui.center(b_close_location)
        pyautogui.click(buttonx, buttony)  # clicks the center of where the button was found
        return True

    return False