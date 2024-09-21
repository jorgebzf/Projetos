import pyautogui

#pedinto informação ao usuário
# email = pyautogui.prompt(text='Digite seu e-mail', title='Informações Obrigatórias')
# print(f'você digitou {email}')

#Confirmar se algo deve ou não acontecer

# resposta = pyautogui.confirm(text='Continua rodando a automação',title='Confirmação',buttons=['Sim','Não','Cancelar'])
    
# if resposta == 'Sim':
#         print('Continuando a automação')
# elif resposta == 'Não':
#         print('Encerrando a automação')
# else:
#         print('Cancelando a automação')

#mascarando a senha
import pyautogui

senha = pyautogui.password(text='Digite sua senha:',title ='dados de login',mask ='*')
print(senha)
