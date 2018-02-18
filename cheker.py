import pyautogui
from time import sleep

import ocv
from commons import close_window

def open_klans():
    pyautogui.press('c')
    sleep(2)

    pyautogui.press('3')
    sleep(2)


def open_klan(name):
    screenWidth, screenHeight = pyautogui.size()
    pyautogui.moveTo(screenWidth // 2, screenHeight // 2)

    for i in range(50):
        klan = ocv.locateCenterOnScreen(name)

        if klan:
            info_pos =  ocv.locateCenterOnScreen('data/klan_info')

            if info_pos:
                pyautogui.click(info_pos[0], info_pos[1])

            break

def get_member_positions():


    member_list = ocv.locateAllOnScreen('data/klan_member_arrow.png')



    for member in member_list:

        pyautogui.click(member[0],member[1])
        #pyautogui.click()

        gorod_pos = ocv.locateOnScreen('data/klan_X.png')

        pyautogui.moveTo(gorod_pos[0], gorod_pos[1])

        close_window()


if __name__ == "__main__":
    ## Set up a 2 second pause after each PyAutoGUI call
    pyautogui.PAUSE = 0.5


    pyautogui.hotkey('alt', 'tab')
    sleep(1)
    cycles = 1
    while(cycles > 0):
        print('cycles: %s'%cycles)

        get_member_positions()

        cycles -= 1
        sleep(300)
    print("end")
    pyautogui.hotkey('alt', 'tab')