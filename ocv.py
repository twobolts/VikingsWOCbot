import cv2
import numpy as np
import pyautogui

def screenshot():
    ''' return np.array object for screenshot '''

    #make screenshot
    screen = pyautogui.screenshot()

    # convert screen to np.array with BGR color style
    return cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)


def locateAllOnScreen(image):
    ''' find all matches of image on the screen'''

    scr = screenshot()

    # read image from file
    template = cv2.imread(image)
    h, w = template.shape[:-1]

    # find all matches in the screen
    res = cv2.matchTemplate(scr, template, cv2.TM_CCOEFF_NORMED)
    threshold = .90
    loc = np.where(res >= threshold)

    res = []
    for pt in zip(*loc[::-1]):  # Switch collumns and rows
        res.append((pt[0],pt[1],w, h))
    return res


def locateOnScreen(image):
    ''' find first matches of image on the screen
        :return
            (x,y,w,h) - if match
            None - if not
    '''
    res = locateAllOnScreen(image)
    if res:
        return res[0]


def locateCenterOnScreen(image):
    ''' find first matches of image on the screen
        :return
            (x,y) - center of found images
            None - if no matches
    '''
    res = locateOnScreen(image)
    print("locateCenter:", image, res)
    if res:
        return center(res)


def center(res):
    ''' return center for (x,y,w,h) tuple '''
    return(res[0]+res[2]//2,res[1]+res[3]//2)


if __name__ == "__main__":
    import pyautogui
    from time import sleep
    pyautogui.hotkey('alt', 'tab')
    sleep(1)

    pyautogui.hotkey('alt', 'tab')



