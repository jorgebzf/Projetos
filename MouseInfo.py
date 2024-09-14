import pyautogui
from time import sleep

#posição algo - use o mouseInfo
#Fazer algo nessa posição
pyautogui.moveTo(1415,492,duration=2)
for i in range(1000):
    sleep(0.1)
    pyautogui.click()