import pyautogui
from time import sleep

from commons import find_and_click, close_window, goto, test, move_to_center
import ocv

def kill_bot(type, level):

    no_energy = False

    #check bot/duh on the screen
    mob_pos = ocv.locateCenterOnScreen('data/map_%s_%s.png' % (type, level))

    # if mob was found attack it
    if mob_pos:
        pyautogui.click(mob_pos[0]+75,mob_pos[1]+75)
        sleep(2)

        res = find_and_click('data/b_atack_normal.png')
        if res:
            if find_and_click('data/b_close_bot_grey.png'):
                find_and_click('data/b_x.png')
                no_energy = True
            find_and_click('data/b_close.png')
        else:
            # Закрыть
            find_and_click('data/b_close_bot.png')

        close_window()

    return mob_pos, no_energy

def attack(type, level):

    ## TODO: fox hard code
    strat_position = (420,540)

    for step in range(0, 91, 5):
        goto(strat_position[0] + step, strat_position[1])
        found, no_energy = kill_bot(type, level)
        if found:
            break

        move_to_center()

    pyautogui.press('M')
    sleep(3)
    return (no_energy == False)


if __name__ == "__main__":

    test(attack, 'bot', '1')