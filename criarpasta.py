import pyautogui

from time import sleep

pyautogui.rightClick(1544,517,duration=0.5)
sleep(0.5)
pyautogui.move(25,150,duration=0.5)
pyautogui.click()
pyautogui.move(-320,-640,duration=0.5)
pyautogui.click()
pyautogui.typewrite="Py - New File"

