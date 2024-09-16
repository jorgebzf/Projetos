#Como usar botóes e atalhos no teclado
import pyautogui

print(pyautogui.KEYBOARD_KEYS)

#como usar combinações de teclas
#move o mouse até um campo
pyautogui.click(1111,444,duration=2)
#seleciona o texto
pyautogui.hotkey('Ctrl','a')
#copia o texto
pyautogui.hotkey('Ctrl','c')
#move até outro ponto
pyautogui.click(1345,345,duration=2)
#cola o texto 
pyautogui.hotkey('Ctrl','v')