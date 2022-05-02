import pyautogui
from selenium import webdriver

DINOSAUR_GAME_URL = "https://elgoog.im/t-rex/"
JUMP_PIXEL_VALUE = (83, 83, 83)
RESTART_BUTTON_COR = (956, 429)
XCOR_1 = 758
XCOR_2 = 777
YCOR = 450
JUMP_COUNT = 0

chrome_driver_path = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(DINOSAUR_GAME_URL)

screenWidth, screenHeight = pyautogui.size()
pyautogui.getWindowsWithTitle("Play T-Rex Dinosaur Game Online - elgooG")[0].maximize()
pyautogui.click(RESTART_BUTTON_COR)
pyautogui.press('space')

game_is_on = True

while game_is_on:
    screen = pyautogui.screenshot()
    px1 = screen.getpixel((XCOR_1, YCOR))
    px2 = screen.getpixel((XCOR_2, YCOR))
    px3 = screen.getpixel((XCOR_1 + 1, YCOR))
    if px1 == JUMP_PIXEL_VALUE or px2 == JUMP_PIXEL_VALUE or px3 == JUMP_PIXEL_VALUE:
        pyautogui.press('space')
        pyautogui.hotkey('ctrl', 'home')
        JUMP_COUNT += 1
        if JUMP_COUNT == 8:
            XCOR_2 += 5
            JUMP_COUNT = 0
