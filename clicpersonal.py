import pyautogui

#click personalizado
pyautogui.click(x=1480,y=410,clicks=1000, 
interval=0.1,button='left',duration=2)
#click na posição atual (com o botão esquerdo)
pyautogui.click()
pyautogui.click(button='left')
pyautogui.click(button='right')
pyautogui.click(button='middle')
#clicar x vezes em algo
pyautogui.click(clicks=10)
#funçoes prontas para click
pyautogui.doubleClick()
pyautogui.rightClickc()
pyautogui.middleClick()
pyautogui.tripleClick()
