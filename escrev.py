import pyautogui
import pyperclip

def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')

pyautogui.moveTo(1237,199,duration=2)
pyautogui.click()
escrever_frase('from mouseinfo import mouseInfo, mouseInfo()')
pyautogui.hotkey('ctrl','s')

