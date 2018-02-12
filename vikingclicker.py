import pyautogui

import cv2
import numpy as np
## Set up a 1.5 second pause after each PyAutoGUI call
pyautogui.PAUSE = 1.5

import ocv

from time import sleep

class resources(object):

    def __init__(self):
        self.res_list = ['farm', 'iron', 'stone', 'tree', 'silver']
        self.current = 'tree'

    def next(self):
        i = self.res_list.index(self.current)
        if i == len(self.res_list)-1:
            self.current = self.res_list[0]
        else:
            self.current = self.res_list[i+1]

        return self.current

def close_window():
    ''' try to find close button "X" and click it
        :returns
            True - if button was found
            False - if button wasn't found
        '''
    b_close_location = ocv.locateOnScreen('b_x.png')

    if b_close_location:
        buttonx, buttony = pyautogui.center(b_close_location)
        pyautogui.click(buttonx, buttony)  # clicks the center of where the button was found
        return True

    return False

def find_and_click(img):
    ''' find the element on the screen and click on it
        :returns
            True if element was found'''
    b_location = ocv.locateCenterOnScreen(img)
    if b_location:
        pyautogui.click(b_location[0], b_location[1])  # close message
        return True

def try_get_resources():
    ''' click on the Захватить
     :returns
        True if ok
        False if not
     '''

    button_location = pyautogui.locateCenterOnScreen('b_get.png')  # returns (x, y) of matching region
    if button_location:
        pyautogui.click(button_location[0], button_location[1])
        sleep(3)

def harvester(res):
    screenWidth, screenHeight = pyautogui.size()

    ## move mouse to get focus on the main window
    pyautogui.moveTo(screenWidth//2, screenHeight//2)

    # Open дозорный
    pyautogui.press('w')
    sleep(3)

    choose_res(res.current)
    button_location = ocv.locateCenterOnScreen('b_get.png')  # returns (x, y) of matching region

    while not button_location:
        ## feetch the resouce
        choose_res(res.next())
        # click on Захватить
        button_location = ocv.locateCenterOnScreen('b_get.png')  # returns (x, y) of matching region

    ## если нашли захватить, тыкаем
    if button_location:
        pyautogui.click(button_location[0], button_location[1])
        sleep(4)

        ## try to send all team to recource
        button = ocv.locateCenterOnScreen('b_choose_all.png')
        if button:
            pyautogui.click(button[0], button[1])

            # click on Send button
            pyautogui.click(button[0]+400, button[1])
            #move_button = pyautogui.locateCenterOnScreen('b_move.png')
            #if move_button:
                #pyautogui.click(move_button[0], move_button[0])
            res.next()

        else:
            ## Обрабатываем ошибку
            # Закрыть
            if not find_and_click('b_close.png'):
                # Назад
                find_and_click('b_back.png')

    close_window()


def choose_res(name, level = None):

    # get information position
    inf_location = ocv.locateCenterOnScreen('l_inf.png')

    if not inf_location:
        print('l_information was not found')
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


def quests():
    screenWidth, screenHeight = pyautogui.size()

    ## move mouse to get focus on the main window
    #pyautogui.moveTo(screenWidth // 2, screenHeight // 2)

    # open quests window
    pyautogui.press('z')

    for i in ['1','2','3']:
        pyautogui.press(i)

        # remove cursor from button
        pyautogui.moveTo(screenWidth // 2, screenHeight // 2)

        # check the button
        find_and_click('b_start.png')  # returns (x, y) of matching region
        # check the button 'Собрать'
        find_and_click('b_sobrat.png')  # returns (x, y) of matching region

    close_window()


def click_help():
    # click on help button
    res = find_and_click('l_help.png')

    if res:
        # click on help all button
        find_and_click('b_help.png')  # returns (x, y) of matching region
        close_window()

def screenshot():
    ''' return np.array object for viking '''

    screen = pyautogui.screenshot()
    screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
    b_location = ocv.locateOnScreen(screen, 'l_window.png')  # returns (x, y) of matching region
    if b_location:
        win_location = [(x + y) for (x, y) in zip(b_location, (-1329, 40, 1325, 870))]
        screen = pyautogui.screenshot(region=(tuple(win_location)))
        screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
    return screen

def kill_mobs():
    print ('kill_mobs')
    pyautogui.press('w')
    sleep(3)
    ##
    choose_res('bot', '2')

    find_and_click('b_info.png')
    sleep(1)

    res = find_and_click('b_atack_normal.png')
    if res:
        if find_and_click('b_close_bot_grey.png'):
            x = ocv.locateAllOnScreen('b_x.png')
            print (x)
            pyautogui.click(ocv.center(x[0]))
    else:
        # Закрыть
        find_and_click('b_close_bot.png')

    close_window()

def get_tmp_imgs():
    # Open дозорный
    pyautogui.press('w')
    sleep(3)
    offset = (-490, 10, 0, -20)
    res = resources()
    tmplt = 5
    for i in range(5):

        choose_res(res.next())
        buttons = ocv.locateAllOnScreen('b_get.png')  # returns (x, y) of matching region

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


def main():
    i = 300
    r = resources()
    while(i != 0):
        quests()

        harvester(r)
        click_help()

        i -= 1
        sleep(300)
    print("end")
    pyautogui.hotkey('alt', 'tab')

if __name__ == "__main__":

    pyautogui.hotkey('alt', 'tab')
    sleep(1)
    main()
    #kill_mobs()
    #smart_harvester()


    #cv_test()

    #img = screenshot()
    #cv2.imwrite('result.png', img)