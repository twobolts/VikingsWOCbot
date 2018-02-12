import cv2
import numpy as np


def test_cv():
    img = cv2.imread('window.png')

    lower_yellow = np.array([0, 100, 0])
    upper_yellow = np.array([179, 255, 255])

    #img = np.array(screen)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(img, lower_yellow, upper_yellow)

    res = cv2.bitwise_and(img, img, mask=mask)

    #kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (50, 5))
    #closed = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    #closed = cv2.erode(closed, kernel, iterations=1)
    #closed = cv2.dilate(closed, kernel, iterations=1)

    # (_, centers, hierarchy) = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # print (centers)

    # (cnts, _) = cv2.findContours(img.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]
    # screenCnt = None

    while True:
        cv2.imshow('Original', img)
        cv2.imshow('mask', mask)
        cv2.imshow('res', res)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

    cv2.destroyAllWindows()

def test_cv2():
    import pyautogui
    from time import sleep
    pyautogui.hotkey('alt', 'tab')
    sleep(1)

    #screen = cv2.imread('window.png')
    ss = pyautogui.screenshot()
    screen = np.array(ss)
    grey_screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)

    #b_location = pyautogui.locateCenterOnScreen('b_get_grey.png')  # returns (x, y) of matching region

    template = cv2.imread('b_sobrat.png')
    h, w = template.shape[:-1]

    res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    threshold = .95
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):  # Switch collumns and rows
        cv2.rectangle(screen, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

        pyautogui.moveTo(pt[0]+w//2,pt[1]+h//2)
        print (pt[0]+w//2,pt[1]+h//2)

    while True:
        cv2.imshow('Original', screen)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

    cv2.destroyAllWindows()

def screenshot():
    ''' return np.array object for viking '''
    import pyautogui
    screen = pyautogui.screenshot()
    screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
    #b_location = locateOnScreen(screen, 'l_window.png')  # returns (x, y) of matching region
    #if b_location:
    #    win_location = [(x + y) for (x, y) in zip(b_location, (-1329, 40, 1325, 870))]
    #    screen = pyautogui.screenshot(region=(tuple(win_location)))
    #    screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
    return screen

def locateOnScreen(image):
    ''' find image on the screen'''
    res = locateAllOnScreen(image)
    if res:
        return res[0]

def locateAllOnScreen(image):
    ''' find image on the screen'''

    scr = screenshot()
    template = cv2.imread(image)
    h, w = template.shape[:-1]

    res = cv2.matchTemplate(scr, template, cv2.TM_CCOEFF_NORMED)
    threshold = .90
    loc = np.where(res >= threshold)
    res = []
    for pt in zip(*loc[::-1]):  # Switch collumns and rows
        res.append((pt[0],pt[1],w, h))
    return res

def locateCenterOnScreen(image):
    res = locateOnScreen(image)
    print('Center: ', image, res)
    if res:
        return center(res)


def center(res):
    return(res[0]+res[2]//2,res[1]+res[3]//2)

if __name__ == "__main__":
    #test_cv()
    #test_cv2()
    import pyautogui
    from time import sleep
    pyautogui.hotkey('alt', 'tab')
    sleep(1)
    print (locateCenterOnScreen('b_sobrat.png') )

    pyautogui.hotkey('alt', 'tab')



'''
    from Xlib.display import Display


    def printWindowHierrarchy(window, indent):
        children = window.query_tree().children
        for w in children:
            print(indent, window.get_wm_class())
            printWindowHierrarchy(w, indent + '-')


    display = Display()
    root = display.screen().root
    printWindowHierrarchy(root, '-')
'''
