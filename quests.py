## class for work with quests window

import pyautogui
from commons import find_and_click, close_window, test
from time import sleep

def run():
    ''' open window quests and click start and collect buttons '''

    # open quests window
    pyautogui.press('z')

    #set PAUSE shorter
    save_pause = pyautogui.PAUSE
    pyautogui.PAUSE = 0.5

    # cycle for quest typess
    for i in ('1', '2', '3'):
        # open quest type
        pyautogui.press(i)

        # click all 'Старт' buttons on the screen
        while find_and_click('data/b_start.png'):
            pass
        # click all 'Собрать' buttons on the screen
        while find_and_click('data/b_sobrat.png'):
            pass

    # restore global PAUSE
    pyautogui.PAUSE = save_pause
    sleep(1)
    close_window()

if __name__ == "__main__":
    test(run)