import cv2
import numpy as np
import pyautogui

def screenshot():
    ''' return np.array object for screenshot '''

    #make screenshot
    screen = pyautogui.screenshot()

    # convert screen to np.array with BGR color style
    return cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)


def locateAllOnScreen(image, screen=None):
    ''' find all matches of image on the screen
        screen can be provided as np.array variable screen
        :return
        list of locations in format: (x,y, width, height)
    '''

    ## get screenshot or screen if it was proveded
    scr = screenshot() if (type(screen) == type(None)) else screen

    # read image from file
    template = cv2.imread(image)
    h, w = template.shape[:-1]

    # find all matches in the screen
    res = cv2.matchTemplate(scr, template, cv2.TM_CCOEFF_NORMED)
    threshold = .94
    loc = np.where(res >= threshold)

    res = []
    for pt in zip(*loc[::-1]):  # Switch collumns and rows
        res.append((pt[0],pt[1],w, h))
    return res


def locateOnScreen(image, screen=None):
    ''' find first matches of image on the screen
        screen can be provided as np.array variable screen
        :return
            (x,y,w,h) - if match
            None - if not
    '''
    res = locateAllOnScreen(image, screen)
    if res:
        return res[0]


def locateCenterOnScreen(image, screen=None):
    ''' find first matches of image on the screen
        screen can be provided as np.array variable screen
        :return
            (x,y) - center of found images
            None - if no matches
    '''
    res = locateOnScreen(image, screen)
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



