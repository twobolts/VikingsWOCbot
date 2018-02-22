## main module with main cycle
#

import pyautogui
## Set up a 2 second pause after each PyAutoGUI call
pyautogui.PAUSE = 2

from time import sleep

from commons import find_and_click, open_game

import quests
import help
import patrol


def main(cycles=1):

    ## open game
    driver = open_game()

    r = patrol.resources()
    hero_ready = False
    shaman_ready = False

    while(cycles > 0):
        print('cycles: %s'%cycles)

        # close window if it's open
        find_and_click('data/b_x.png')

        #main part
        quests.run()
        if hero_ready:
            hero_ready = patrol.attack('bot', '1')
        if shaman_ready:
            shaman_ready = patrol.attack('duh', '1')
        patrol.harvester(r)
        help.run()

        if cycles%40 == 0:
            hero_ready = True
            shaman_ready = True

        # reset application if connection is broke
        find_and_click('data/reset_b.png')

        cycles -= 1
        sleep(360)
    print("end")
    driver.close()

if __name__ == "__main__":

    main(110)
