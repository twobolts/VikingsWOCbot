import pyautogui

import cv2
import numpy as np
## Set up a 1.5 second pause after each PyAutoGUI call
pyautogui.PAUSE = 1.0

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
    sleep(4)

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
            #close_window()

            # Закрыть
            b_location = ocv.locateCenterOnScreen('b_close.png')
            if b_location:
                pyautogui.click(b_location[0], b_location[1]) # close message

            # Назад
            b_location = ocv.locateCenterOnScreen('b_back.png')
            if b_location:
                pyautogui.click(b_location[0], b_location[1])  # close message

    close_window()


def choose_res(name):

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

def quests():
    screenWidth, screenHeight = pyautogui.size()

    ## move mouse to get focus on the main window
    #pyautogui.moveTo(screenWidth // 2, screenHeight // 2)

    # open quests window
    pyautogui.press('z')

    for i in ['1','2','3']:
        pyautogui.press(i)

        pyautogui.moveTo(screenWidth // 2, screenHeight // 2)
        # check the button собрать
        button_location = ocv.locateCenterOnScreen('b_sobrat.png')  # returns (x, y) of matching region
        if button_location:
            pyautogui.click(button_location[0], button_location[1])

        pyautogui.moveTo(screenWidth // 2, screenHeight // 2)

        # check the button start
        button_location = ocv.locateCenterOnScreen('b_start.png')  # returns (x, y) of matching region
        if button_location:
            pyautogui.click(button_location[0], button_location[1])

    close_window()
    #pyautogui.click(500, 500)

def click_help():
    screenWidth, screenHeight = pyautogui.size()

    button_location = ocv.locateCenterOnScreen('l_help.png')  # returns (x, y) of matching region
    if button_location:
        pyautogui.click(button_location[0], button_location[1])

        pyautogui.moveTo(screenWidth // 2, screenHeight // 2)

        b_help_all = ocv.locateCenterOnScreen('b_help.png')  # returns (x, y) of matching region
        if b_help_all:
            pyautogui.click(b_help_all[0], b_help_all[1])
        close_window()
        #pyautogui.click(500, 500)

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

def cv_test():

    b_location = pyautogui.locateOnScreen('l_window_l.png')  # returns (x, y) of matching region

    screen = pyautogui.screenshot()
    if b_location:
        win_location = [(x + y) for (x, y) in zip(b_location, (-1329, 40, 1325, 870))]
        screen = pyautogui.screenshot(region=( tuple (win_location) ))
        screen = pyautogui.screenshot('window_lin.png', region=(tuple(win_location)))

    lower_yellow = np.array([0,100,50])
    upper_yellow = np.array([30,255,255])

    img = np.array(screen)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(img, lower_yellow, upper_yellow)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (50, 5))
    closed = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    closed = cv2.erode(closed, kernel, iterations=1)
    closed = cv2.dilate(closed, kernel, iterations=1)

    #(_, centers, hierarchy) = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #print (centers)

    #(cnts, _) = cv2.findContours(img.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]
    #screenCnt = None

    while True:
        cv2.imshow('Original', img)
        cv2.imshow('mask', mask)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

    cv2.destroyAllWindows()

def main():
    i = 500
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

    #cv_test()

    #img = screenshot()
    #cv2.imwrite('result.png', img)