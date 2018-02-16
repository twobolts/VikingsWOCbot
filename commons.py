## common functions

import ocv
import pyautogui
from time import sleep


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


def goto(x, y):
    ''' open the map location by coordinate (x, y)
        :usage
            goto(256, 256)
        :return
            True if successful, false if not
    '''

    ## open goto window
    pyautogui.press('N')
    sleep(2)

    # get button перейти
    b_screen_pos = ocv.locateCenterOnScreen('data/goto.png')

    if b_screen_pos:
        # set X
        pyautogui.doubleClick(b_screen_pos[0] - 150, b_screen_pos[1] - 120, interval=0.25)
        pyautogui.typewrite(str(x))

        # set Y
        pyautogui.doubleClick(x=(b_screen_pos[0] + 30), y=(b_screen_pos[1] - 120), interval=0.25)
        pyautogui.typewrite(str(y))

        # goto
        pyautogui.click(b_screen_pos[0], b_screen_pos[1])

        return True
    return False
