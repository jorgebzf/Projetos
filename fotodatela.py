import pyautogui
#tirar foto da tela inteira
pyautogui.screenshot('tela.jpg')
#tirar foto de uma regição da tela
pyautogui.screenshot('partedatela.jpg',region=(100,100,300,500))