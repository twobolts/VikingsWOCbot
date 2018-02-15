## class for work with quests window

import pyautogui
from time import sleep

from commons import find_and_click, close_window
import ocv
import cv2
import numpy as np


class resources(object):

    def __init__(self):
        self.res_list = ['farm', 'iron', 'tree', 'stone', 'silver', 'bot_house']
        self.current = 'farm'

    def next(self):
        i = self.res_list.index(self.current)
        if i == len(self.res_list)-1:
            self.current = self.res_list[0]
        else:
            self.current = self.res_list[i+1]

        return self.current


def harvester(res):
    screenWidth, screenHeight = pyautogui.size()
    ## move mouse to get focus on the main window
    pyautogui.moveTo(screenWidth//2, screenHeight//2)

    # Open дозорный
    pyautogui.press('w')
    sleep(3)

    choose_res(res.current)
    button_location = ocv.locateCenterOnScreen('data/b_get.png')  # returns (x, y) of matching region

    limit = 5;
    while not button_location and limit:
        ## feetch the resouce
        choose_res(res.next())
        # click on Захватить
        button_location = ocv.locateCenterOnScreen('data/b_get.png')  # returns (x, y) of matching region
        limit -= 1

    ## если нашли захватить, тыкаем
    if button_location:
        pyautogui.click(button_location[0], button_location[1])
        sleep(3)

        ## try to send all team to recource
        button = ocv.locateCenterOnScreen('data/b_move.png')
        if button:

            army_offset = [430, 320, 210, 117]
            #chouse part of army

            for i in army_offset:
                pyautogui.click(button[0]-113, button[1] - i)
                #pyautogui.press('9', presses=4)

            # click on Send button
            pyautogui.click(button[0], button[1])
            res.next()

        else:
            ## Обрабатываем ошибку
            # Закрыть
            if not find_and_click('data/b_close.png'):
                # Назад
                find_and_click('data/b_back.png')

    close_window()


def choose_res(name, level=None):

    # get information position
    inf_location = ocv.locateCenterOnScreen('data/l_inf.png')

    if not inf_location:
        print('l_information on choose_res window is not found')
        return

    # click on the list of elements
    res_list_x = inf_location[0] + 250
    res_list_y = inf_location[1]

    pyautogui.click(res_list_x, res_list_y)

    if name is 'city':
        pyautogui.click(res_list_x, res_list_y + 30)
    elif name is 'farm':
        pyautogui.click(res_list_x, res_list_y + 60)
    elif name is 'gold':
        pyautogui.click(res_list_x, res_list_y + 90)
    elif name is 'gold_god':
        pyautogui.click(res_list_x, res_list_y + 120)
    elif name is 'iron':
        pyautogui.click(res_list_x, res_list_y + 150)
    elif name is 'silver':
        pyautogui.click(res_list_x, res_list_y + 170)
    elif name is 'stone':
        pyautogui.click(res_list_x, res_list_y + 200)
    elif name is 'tree':
        pyautogui.click(res_list_x, res_list_y + 230)
    elif name is 'bot':
        pyautogui.click(res_list_x, res_list_y + 260)
    elif name is 'bot_house':
        pyautogui.click(res_list_x, res_list_y + 290)
    else:
        pyautogui.click()

    if level:
        # click on the level of elements
        res_list_x = inf_location[0] + 500
        pyautogui.click(res_list_x, res_list_y)

        if level is 'all':
            pyautogui.click(res_list_x, res_list_y + 30)
        elif level is '1':
            pyautogui.click(res_list_x, res_list_y + 60)
        elif level is '2':
            pyautogui.click(res_list_x, res_list_y + 90)
        elif level is '3':
            pyautogui.click(res_list_x, res_list_y + 120)
        elif level is '4':
            pyautogui.click(res_list_x, res_list_y + 150)
        elif level is '5':
            pyautogui.click(res_list_x, res_list_y + 170)
        elif level is '6':
            pyautogui.click(res_list_x, res_list_y + 200)
        else:
            pyautogui.click()


def kill_mobs(level):
    print ('kill_mobs')
    pyautogui.press('w')
    sleep(3)
    ##
    choose_res('bot', level=str(level))

    find_and_click('data/b_info.png')
    sleep(1)

    res = find_and_click('data/b_atack_normal.png')
    if res:
        if find_and_click('data/b_close_bot_grey.png'):
            x = ocv.locateAllOnScreen('data/b_x.png')
            print (x)
            pyautogui.click(ocv.center(x[0]))
    else:
        # Закрыть
        find_and_click('data/b_close_bot.png')

    close_window()
    return res

def get_tmp_imgs():
    # Open дозорный
    pyautogui.press('w')
    sleep(3)
    offset = (-490, 10, 0, -20)
    res = resources()
    tmplt = 5
    for i in range(5):

        choose_res(res.next())
        buttons = ocv.locateAllOnScreen('data/b_get.png')  # returns (x, y) of matching region

        for b_location in buttons:
            pyautogui.moveTo(b_location[0],b_location[1])

            b_location = [x+y for (x,y) in zip(b_location,offset)]

            #берем кол-во в локации
            img = pyautogui.screenshot(region=(tuple(b_location)))
            screen = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

            tmplt +=1
            cv2.imwrite('tmp_%d.png' %(tmplt), screen)

    #pyautogui.moveRel(xOffset=-490, yOffset=10)
    sleep(4)

def smart_harvester():
    im = cv2.imread('tmp_5.png')
    im3 = im.copy()

    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    lower_red = np.array([0, 100, 0])
    upper_red = np.array([179, 255, 255])

    mask = cv2.inRange(im, lower_red, upper_red)
    res = cv2.bitwise_and(im, im, mask=mask)

    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)

    #################      Now finding Contours         ###################

    im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    #print (contours)
    samples = np.empty((0, 100))
    responses = []
    keys = [i for i in range(48, 58)]

    for cnt in contours:
        if cv2.contourArea(cnt) > 10:
            [x, y, w, h] = cv2.boundingRect(cnt)
            print ([x, y, w, h])
            if h > 10:
                cv2.rectangle(im, (x, y), (x + w, y + h), (0, 0, 255), 1)
            #roi = thresh[y:y + h, x:x + w]
            #roismall = cv2.resize(roi, (10, 10))
            #cv2.imshow('norm', im)

    while True:
        cv2.imshow('im3', im)
        cv2.imshow('norm', thresh)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

def kill_duh(level):
    x = ocv.locateCenterOnScreen('data/map_duh_%s.png' % level)

    if x:
        pyautogui.click(x[0]+75,x[1]+75)
        sleep(2)

        res = find_and_click('data/b_atack_normal.png')
        if res:
            if find_and_click('data/b_close_bot_grey.png'):
                x = ocv.locateAllOnScreen('data/b_x.png')
                pyautogui.click(ocv.center(x[0]))

        else:
            # Закрыть
            find_and_click('data/b_close_bot.png')

        close_window()

        return True

def find_on_map(pos):
    pyautogui.press('N')
    sleep(2)

    x = ocv.locateCenterOnScreen('data/goto.png')

    if x:
        #set X
        pyautogui.click(x[0]-150, x[1]-120)
        pyautogui.typewrite(str(pos[0]))

        # set Y
        pyautogui.click(x[0]+30, x[1] - 120)
        pyautogui.click(x[0] + 30, x[1] - 120)
        pyautogui.typewrite(str(pos[1]))

        #goto
        pyautogui.click(x[0], x[1])

        return True

    return False

def shaman(level):
    strat_position = (420,540)

    for step in range(0, 91, 5):
        position = (strat_position[0] + step, strat_position[1])
        find_on_map(position)
        if kill_duh(level):
            return True


if __name__ == "__main__":
    ## Set up a 2 second pause after each PyAutoGUI call
    pyautogui.PAUSE = 2


    pyautogui.hotkey('alt', 'tab')
    sleep(1)
    cycles = 1
    while(cycles > 0):
        print('cycles: %s'%cycles)
        close_window()

        #kill_mobs()
        #shaman(1)
        harvester(resources())

        cycles -= 1
        sleep(300)
    print("end")
    pyautogui.hotkey('alt', 'tab')