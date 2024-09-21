import pyautogui
import webbrowser
from time import sleep

def logout():
    pyautogui.click(1385,614,duration=1)
    pyautogui.click(1874,108,duration=1)
    pyautogui.click(1761,352,duration=1)
# 1- Navegar até o site https://www.intagram.com
while True:
    webbrowser.open_new_tab('https://instagram.com')
    sleep(1)
    #2 - Entrar com o meu usuário
    pyautogui.click(1529,362,duration=1)
    sleep(1)
    #3 - Entrar com a minha senha
    pyautogui.typewrite('usuarioinsta')
    sleep(1)
    pyautogui.typewrite('senhapadrao')
    sleep(1)
    #4 - Clicar em "log in"
    pyautogui.click(1567,445,duration=1)
    sleep(20)
    #5 - Clicar em "Not now" para não salvar navegador
    pyautogui.click(1590,603,duration=1)
    #6 - Fechar janela de "salvar senha"
    pyautogui.click(1662,88,duration=1)
    sleep(20)
    #7 - Pesquisar pela página
    pyautogui.click(1626,105,duration=1)
    sleep(1)
    #8 - Entrar na página
    pyautogui.typewrite('nike')
    sleep(20)
    pyautogui.move(0,15)
    pyautogui.click()
    sleep(1)
    #9 - Clicar na postagem mais recente
    pyautogui.click(1398,595,duration=1)
    sleep(10)
    #10 - Verifica se já curti ou não aquela postagem
    #dica - retirar foto da imagem do coração de curtida, se estiver vermelho já foi
    #curtido, se não ainda não foi
    pyautogui.locateCenterOnScreen('coracaobco.png')
    sleep(1)
    #11 - Se ja tiver curtido, fazer nada, e pausar o bot por 24hs
    if coracaobco is not None:
        logout()
        sleep(86400)


    #12 - se não tiver curtido, curtir a "foto"
    elif coracaobco == None:
        pyautogui.click(1468,746,duration=1)   
        sleep(5)
        pyautogui.click(1505,749,duration=1)
        sleep(3)
        pyautogui.click(1568,834,duration=1)
        sleep(1)
        pyautogui.typewrite("Gostei da foto!")
    #13 - Se não tiver curtido, comentar na "foto"
        logout()
    #14 - Pausar por 24 horas
    sleep(86400)
    #15 - Apos 24 hs rodar tudo de novo



