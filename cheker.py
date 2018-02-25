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
    import Player

    member_list = ocv.locateAllOnScreen('data/klan_member_arrow.png')

    for member in member_list:

        pyautogui.click(member[0],member[1])
        #pyautogui.click()

        gorod_pos = Player.get_player_positions()
        print(gorod_pos)

        #pyautogui.moveTo(gorod_pos[0], gorod_pos[1])

        close_window()

def check_sheld(list_of_positions):
    from commons import goto, close_window

    res = []
    for pos in list_of_positions:

        goto(pos[0],pos[1])

        gor_pos = ocv.locateCenterOnScreen('data/map_gorod.png')
        pyautogui.click(gor_pos[0],gor_pos[1]-450)

        #TODO: check sheld
        is_sheld = ocv.locateCenterOnScreen('data/map_sheld.png')

        if not is_sheld:
            print(pos)

        close_window()


if __name__ == "__main__":
    from commons import test

    test(get_member_positions)