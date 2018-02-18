import cv2
import numpy as np

import pyautogui
from time import sleep

import ocv
from commons import close_window

def get_player_positions():
    offsetX = (16, 0, 11, -3)
    offsetY = (63, 0, 11, -3)

    b_location = ocv.locateOnScreen('data/klan_X.png')

    #pyautogui.moveTo(b_location[0], b_location[1])

    b_location_X = [x + y for (x, y) in zip(b_location, offsetX)]
    b_location_Y = [x + y for (x, y) in zip(b_location, offsetY)]

    # берем кол-во в локации
    x_pos = pyautogui.screenshot(region=(tuple(b_location_X)))
    y_pos = pyautogui.screenshot(region=(tuple(b_location_Y)))

    return (np.array(x_pos), np.array(y_pos))

def smart_harvester():
    im_x, im_y = get_player_positions()

    im = []
    im.append(im_x[:, 0:7])
    im.append(im_x[:, 8:15])
    im.append(im_x[:, 15:])

    res = ''
    for i in range(3):
        k = get_number(im[i])
        res += str(k)

    print('X:', res)

    im = []
    im.append(im_y[:, 0:7])
    im.append(im_y[:, 8:15])
    im.append(im_y[:, 15:])

    res = ''
    for i in range(3):
        k = get_number(im[i])
        res += str(k)

    print('Y:', res)

    while True:
        cv2.imshow('im1', im[0])
        cv2.imshow('im2', im[1])
        cv2.imshow('im3', im[2])

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

def get_number(image):
    print('get_number!')
    for i in range(10):
        template = cv2.imread('pos_%d.png' %i)
        res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
        threshold = .95
        print (i, res)
        if (res >= threshold).any():
            return i

if __name__ == "__main__":
    ## Set up a 2 second pause after each PyAutoGUI call
    pyautogui.PAUSE = 0.5


    pyautogui.hotkey('alt', 'tab')
    sleep(1)
    cycles = 1
    while(cycles > 0):
        print('cycles: %s'%cycles)

        smart_harvester()

        cycles -= 1
        # sleep(300)
    print("end")
    pyautogui.hotkey('alt', 'tab')