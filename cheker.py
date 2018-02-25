import pyautogui
from time import sleep

import ocv
from commons import close_window, move_to_center

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

def scroll_clan():

    for i in range(5):
        pyautogui.scroll(-35)

def get_member_positions():
    import Player
    member_pos = []

    end_of_list = False
    while not end_of_list:

        member_list = ocv.locateAllOnScreen('data/klan_member_arrow.png')

        for member in member_list:

            pyautogui.click(member[0],member[1])

            gorod_pos = Player.get_player_positions()
            x = ''.join([str(x) for x in gorod_pos[0]])
            y = ''.join([str(x) for x in gorod_pos[1]])

            if member_pos.count((x,y))>2:
                end_of_list = True
                break

            member_pos.append((x,y))

            close_window()

        move_to_center()
        pyautogui.scroll(-30)

    while close_window():
        move_to_center()

    member_pos = list(set(member_pos))
    print('member_pos: ', member_pos)
    return check_sheld(member_pos)

def check_sheld(list_of_positions):
    from commons import goto, close_window

    res = []
    for pos in list_of_positions:

        goto(pos[0],pos[1])

        gor_pos = ocv.locateCenterOnScreen('data/map_gorod.png')
        pyautogui.click(gor_pos[0],gor_pos[1]-400)
        sleep(2)

        #TODO: check sheld
        is_sheld = ocv.locateCenterOnScreen('data/map_sheld.png')

        if not is_sheld:
            res.append(pos)

        close_window()
    return res

if __name__ == "__main__":
    from commons import test

    print (test(get_member_positions))

    #test(get_member_positions)