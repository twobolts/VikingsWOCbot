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


def get_player_positions(screen=None):
    ''' find the player position on the screen abd return with X and Y position '''

    screen = ocv.screenshot() if (type(screen) == type(None)) else screen

    ## get X: screenshot
    x_pos = ocv.locateOnScreen('data/klan_X.png', screen)

    if x_pos:
        xy_im = screen[x_pos[1]:x_pos[1]+10, x_pos[0]+11:x_pos[0]+100]

        digits = find_digits(xy_im)

        # for Y find_digits return None, so just split by None
        split = digits.index(None)

        x = digits[0:split]
        y = digits[split+1:]

        return (x,y)

def image2digit(image):
    ''' convert image to digit for player position'''
    #print('get_number!')
    for i in range(10):
        res = cv2.matchTemplate(image, pos_template[i], cv2.TM_CCOEFF_NORMED)
        threshold = .95
        #print (i, res)
        if (res >= threshold).any():
            return i

def find_digits(img):
    ''' find all symbols in the img
        :return
            list of digits or None, for example [2,6,6,None,7,3,4]'''

    ## 
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(grey, 150, 255, cv2.THRESH_BINARY)

    #thresh = mask.copy()

    ## set collumne to white if it has at list one white pixel
    transpose_mask = mask.transpose()
    for i, x in enumerate (transpose_mask):
        if (x == 255).any():
            transpose_mask[i]=255

    # find counters
    im2, contours, hierarchy = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    #im = img.copy()
    # find counters for each digit and
    res = []
    for cnt in contours[::-1]:
        if cv2.contourArea(cnt) > 15:
            [x, y, w, h] = cv2.boundingRect(cnt)
            #cv2.rectangle(im, (x, y), (x + w, y + h), (0, 0, 255), 1)

            res.append(image2digit(img[:,x-1:x+7]))

    # while True:
    #     cv2.imshow('im', im)
    #     cv2.imshow('thresh', thresh)
    #     cv2.imshow('mask', mask)
    #
    #     k = cv2.waitKey(5) & 0xFF
    #     if k == 27:
    #         break

    return res

def test_():
    wn = cv2.imread('window.png')

    x_pos = ocv.locateAllOnScreen('data/klan_X.png', wn)

    x_pos = x_pos[0]
    print(x_pos)
    im = wn[x_pos[1]:x_pos[1]+10, x_pos[0]+11:x_pos[0]+100]
    x_img = im.copy()

    ## find on the image
    grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey, (5, 5), 0)
    _, thresh = cv2.threshold(grey, 127, 255, cv2.THRESH_BINARY)
    #thresh = cv2.adaptiveThreshold(blur, 225, 1, cv2.THRESH_BINARY, 11, 2)

    mask = thresh.transpose()

    x_line = 0
    for i, x in enumerate (mask):
        #print(x, (x == 0).all())

        if (x != 0).any():
            mask[i]=255

            if not x_line:
                x_line = i

    im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours[::-1]:
        if cv2.contourArea(cnt) > 20:
            [x, y, w, h] = cv2.boundingRect(cnt)
            #print ([x, y, w, h])
            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 0, 255), 1)

            print('res', image2digit(x_img[:,x-1:x+7]))

    while True:
        cv2.imshow('img1', im)
        cv2.imshow('thresh', thresh)
        #cv2.imshow('blur', mask)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

if __name__ == "__main__":
    wn = cv2.imread('window1.png')

    print(get_player_positions(wn))





