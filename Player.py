import cv2
import numpy as np

import pyautogui
from time import sleep

import ocv
from commons import close_window

pos_template = []
for i in range(10):
    pos_template.append(cv2.imread('data/player_pos/pos_%d.png' %i))

def test_position():

    offsetX = (0, 0, 75, -3)

    creen = cv2.imread('window.png')

    b_location = ocv.locateAllOnScreen('data/klan_X.png', creen)[0]

    #b_location = ocv.locateOnScreen('data/klan_X.png')
    b_location_X = [x + y for (x, y) in zip(b_location, offsetX)]

    #im = pyautogui.screenshot(region=(tuple(b_location_X)))

    im = creen[b_location_X[1]:b_location_X[1]+b_location_X[3],
         b_location_X[0]:b_location_X[0]+b_location_X[2]]

    im = np.array(im)

    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (3, 7), 0)
    #thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)
    thresh = cv2.adaptiveThreshold(blur, 255, 1, cv2.THRESH_BINARY, 11, 2)

    #################      Now finding Contours         ###################

    im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    #print (contours)
    samples = np.empty((0, 100))
    responses = []
    keys = [i for i in range(48, 58)]

    for cnt in contours:
        if cv2.contourArea(cnt) > 20:
            [x, y, w, h] = cv2.boundingRect(cnt)
            print ([x, y, w, h])
            if h > 7:
                cv2.rectangle(im, (x, y), (x + w, y + h), (0, 0, 255), 1)
            #roi = thresh[y:y + h, x:x + w]
            #roismall = cv2.resize(roi, (10, 10))
            #cv2.imshow('norm', im)

    while True:
        cv2.imshow('im3', im)
        cv2.imshow('blur', blur)
        cv2.imshow('thresh', thresh)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break


def get_player_positions():
    ''' find the player position on the screen abd return with X and Y position '''

    offsetX = (16, 0, 11, -3)
    offsetY = (61, 0, 11, -3)

    b_location = ocv.locateOnScreen('data/klan_X.png')

    b_location_X = [x + y for (x, y) in zip(b_location, offsetX)]
    b_location_Y = [x + y for (x, y) in zip(b_location, offsetY)]

    # берем кол-во в локации
    x_pos = pyautogui.screenshot(region=(tuple(b_location_X)))
    y_pos = pyautogui.screenshot(region=(tuple(b_location_Y)))

    x = pos2number(np.array(x_pos))
    y = pos2number(np.array(y_pos))

    return (x,y)

def pos2number(xy_pos_img):
    ''' convert X/Y position image(123) to str 123 '''

    im = [xy_pos_img[:, 0:7],
          xy_pos_img[:, 7:14],
          xy_pos_img[:, 15:21]]

    res = ''
    for i in range(3):
        k = image2digit(im[i])
        res += str(k)

    while True:
        cv2.imshow('img1', im[0])
        cv2.imshow('img2', im[1])
        cv2.imshow('img13', im[2])

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

    return res

def smart_harvester():
    im_x, im_y = get_player_positions()

    x = pos2number(im_x)
    y = pos2number(im_y)

def image2digit(image):
    ''' convert image to digit for player position'''
    print('get_number!')
    for i in range(10):
        res = cv2.matchTemplate(image, pos_template[i], cv2.TM_CCOEFF_NORMED)
        threshold = .95
        print (i, res)
        if (res >= threshold).any():
            return i

if __name__ == "__main__":
    ## Set up a 2 second pause after each PyAutoGUI call
    pyautogui.PAUSE = 0.5


    #pyautogui.hotkey('alt', 'tab')
    #sleep(1)
    cycles = 1
    while(cycles > 0):
        print('cycles: %s'%cycles)

        print (test_position())

        cycles -= 1
        # sleep(300)
    print("end")
    #pyautogui.hotkey('alt', 'tab')