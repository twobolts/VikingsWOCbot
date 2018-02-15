## main module with main cycle
#

import pyautogui
## Set up a 2 second pause after each PyAutoGUI call
pyautogui.PAUSE = 2

from time import sleep

from commons import close_window

import quests
import help
import patrol


def main(cycles=1):

    ## TODO: add method to switc on game browser window
    pyautogui.hotkey('alt', 'tab')
    sleep(1)

    r = patrol.resources()
    hero_flag = True
    while(cycles > 0):
        print('cycles: %s'%cycles)
        close_window()

        quests.run()
        if not hero_flag:
            hero_flag = patrol.kill_mobs('2')
        patrol.harvester(r)
        help.run()

        if cycles%15 == 0:
            hero_flag = False

        cycles -= 1
        sleep(360)
    print("end")
    pyautogui.hotkey('alt', 'tab')

if __name__ == "__main__":

    main(2)
