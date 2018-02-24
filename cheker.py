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

    oops = [  (269, 463)
            , (281, 574)
            , (292, 233)
        , (141, 33)
        , (443, 688)
        , (336, 386)
        , (42, 578)
        , (187, 488)
        , (474, 16)
        , (510, 954)
        , (239, 876)
        , (269, 466)
        , (205, 273)
        , (225, 389)
        , (270, 465)
        , (233, 459)
        , (443, 778)
        , (432, 282)
        , (338, 1003)
        , (413, 666)
        , (252, 524)
        , (239, 484)
        , (145, 953)
        , (220, 451)
        , (414, 742)
        , (65, 368)
        , (231, 171)
        , (146, 213)
        , (267, 118)
        , (322, 274)
              ]

    test(check_sheld, oops)