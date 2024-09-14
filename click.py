#Botão Click
import pyautogui

#Click personalizado
pyautogui.click(x=1700,y=200,clicks=1000,interval=0.1,button='left',duration=2)

#click na posição atual (com o botão esquerdo)
pyautogui.click()
pyautogui.click(button='left')
pyautogui.click(button='right')
pyautogui.click(button='middle')
#clicar x vezes
pyautogui.click(clicks=10)
# Funções prontas para clicks
pyautogui.doubleClick()
pyautogui.rightClick()
pyautogui.middleClick()
pyautogui.tripleClick()