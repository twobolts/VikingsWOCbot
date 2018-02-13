## class for work with quests window

import pyautogui

from commons import find_and_click, close_window

def run():
    ''' open window quests and click start and collect buttons '''

    ## screen size
    screenWidth, screenHeight = pyautogui.size()

    # open quests window
    pyautogui.press('z')

    # cycle for quest types
    for i in ('1', '2', '3'):
        # open quest type
        pyautogui.press(i)

        # remove cursor from button
        pyautogui.moveTo(screenWidth // 2, screenHeight // 2)

        # click 'Старт'
        find_and_click('data/b_start.png')  # returns (x, y) of matching region
        # click 'Собрать'
        find_and_click('data/b_sobrat.png')  # returns (x, y) of matching region

    close_window()