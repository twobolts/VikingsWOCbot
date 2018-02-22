## common functions

import ocv
import pyautogui
import time

def find_and_click(img):
    ''' find the element on the screen and click on it
        :returns
            True if element was found'''
    b_location = ocv.locateCenterOnScreen(img)
    if b_location:
        pyautogui.click(b_location[0], b_location[1])
        return True

def close_window():
    ''' try to find close button "X" and click it
        :returns
            True - if button was found
            False - if button wasn't found
        '''
    return find_and_click('data/b_x.png')

def test(func, *args, cycles=1, sleep=0):
    ''' run func'''

    pyautogui.PAUSE = 2
    ## screen size
    screenWidth, screenHeight = pyautogui.size()

    print('start test')
    pyautogui.hotkey('alt', 'tab')
    time.sleep(1)
    # set cursor on the center
    pyautogui.moveTo(screenWidth // 2, screenHeight // 2)
    while(cycles > 0):
        print('cycles: %s'%cycles)

        func(*args)

        cycles -= 1
        time.sleep(sleep)
    pyautogui.hotkey('alt', 'tab')

def goto(x, y):
    ''' open the map location by coordinate (x, y)
        :usage
            goto(256, 256)
        :return
            True if successful, false if not
    '''

    ## open goto window
    pyautogui.press('N')
    time.sleep(3) # wait while map will be opened

    #set PAUSE shorter
    save_pause = pyautogui.PAUSE
    pyautogui.PAUSE = 0.5

    # get button перейти
    b_screen_pos = ocv.locateCenterOnScreen('data/goto.png')

    if b_screen_pos:
        # set X
        pyautogui.doubleClick(b_screen_pos[0] - 150, b_screen_pos[1] - 120, interval=0.25)
        pyautogui.typewrite(str(x))

        # set Y
        pyautogui.doubleClick(x=(b_screen_pos[0] + 30), y=(b_screen_pos[1] - 120), interval=0.25)
        pyautogui.typewrite(str(y))

        # goto
        pyautogui.click(b_screen_pos[0], b_screen_pos[1])

        return True

    # restore global PAUSE
    pyautogui.PAUSE = save_pause

    return False

def open_game():
    ''' open game by webdriver'''
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.options import Options

    from time import sleep

    # maximize window
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome('/home/vladimir/myProjects/chromedriver/chromedriver', chrome_options=options)

    # open domain
    driver.get("https://plarium.com/ru")

    # load previous session
    driver.add_cookie({'name': 'portal.auth.v31',
                       'value': '55BAD2294FDECAD20E19E0071EC114054754673F56D32958E945708B7FA7A6DD8BF8BE80898DE2BE4B1ADCB83B6E82C055F9E695A7598CF1485C142CC0D59E0FAE54905F0811FE884E113038F18635BDD5CF75F763B26156068124A8890E310BA0FD10000676432E7E0E2C45593142A57836990C2D8E56E6B58BEE5BC97C6BDC8444BCEDE448C6EBDC39F032E46F266C2850FC0FC23089D7B640B1DDFB1EC5ABBB924209426B6238B227FCB5183355AD75C8C85C5956BF495B60D7641D638F8F847B0861752BC7347A5A3A9B3B74CCC410E73D1EC5567690E97F5F9C38135DA19A2FBCACC8780752C41E4414F024B4A90FAD99FADDCAAEDD9F1F7F34ED661E8AEA965E02F134D1AFBFAEE30C23F4A401A2F70828'})


    # open game
    driver.get("https://plarium.com/ru/igri-strategii/vikings-war-of-clans/igra/")

    elem = driver.find_element_by_xpath('//button[text()="OK"]')
    elem.click()

    # wait for game loading
    sleep(60)


    # # assert "Python" in driver.title
    # #elem = driver.find_element_by_class_name("PBSgSV")
    # elem = driver.find_element_by_xpath('//button[text()="Войди"]')
    # elem.click()
    #
    # mail = driver.find_element_by_id('email')
    # mail.send_keys('vladimir.tuboltsev@gmail.com')
    # #elem = elem.find_element_by_tag_name("data-qa-entity")
    # #elem = elem.find_element_by_tag_name('button')
    #
    # password = driver.find_element_by_id('password')
    # password.send_keys('Spawn123')
    # password.send_keys(Keys.ENTER)
    return driver