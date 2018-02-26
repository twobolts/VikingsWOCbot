import pyautogui
from time import sleep

from commons import find_and_click, close_window, goto, test, move_to_center
import ocv

last_bot_position = {}

## TODO: fix hard code
strat_position = (420, 540)

def kill_bot(type, level):

    no_energy = False

    #check bot/duh on the screen
    mob_pos = ocv.locateCenterOnScreen('data/map_%s_%s.png' % (type, level))

    # if mob was found attack it
    if mob_pos:
        pyautogui.click(mob_pos[0]+65,mob_pos[1]+40)
        sleep(4)

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
    ''' atack the bot '''

    #check last successful position
    bot_pos = last_bot_position.get(type+level)
    if bot_pos:
        goto(bot_pos[0], bot_pos[1])
        sleep(1)
        found, no_energy = kill_bot(type, level)
        if found:
            last_bot_position[type+level] = (bot_pos[0], bot_pos[1])
    else:
        # find new position
        for step in range(0, 91, 5):
            move_to_center()
            goto(strat_position[0] + step, strat_position[1])
            found, no_energy = kill_bot(type, level)
            if found:
                last_bot_position[type+level] = (strat_position[0] + step, strat_position[1])
                break

    return (no_energy == False)


if __name__ == "__main__":

    flag = True
    i = 0
    while flag:
        i += 1
        print(i, flag)
        flag = test(attack, 'bot', '1', sleep=360)