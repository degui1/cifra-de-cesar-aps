from modules.CifraCesar import CifraCesar
from telnetlib import SGA
from PySimpleGUI import PySimpleGUI as sg

# layout
sg.theme('reddit')
layout = [
    [sg.Text('Digite a chave da cifra')],
    [sg.Input(key='key')],
    [sg.Text('Mensagem')],
    [sg.Input( key= 'message')],
    [sg.Text('Criptografia')],
    [sg.Input( key= 'cifra')],
    [sg.Button('Criptografar')],
    [sg.Button('Descriptografar')],

]


# Window
janela= sg.Window('Verificação de acesso', layout)
#ler Dados

while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Criptografar':
        crypt = CifraCesar(int(valores ['key']))
        messageEncrypted = crypt.encryptMessage(valores ['message'])
        print(messageEncrypted)
        print("Acesso criado!")
    if eventos == 'Descriptografar':
        if valores ['cifra'] == '':
            crypt.decryptMessage()
            print(crypt.getMessage())
            print("Acesso verificado")
        elif valores ['cifra'] == messageEncrypted:
            crypt = CifraCesar(int(valores ['key'])*-1)
            messageEncrypted = crypt.encryptMessage(valores ['cifra'])
            print(messageEncrypted)
            print("Acesso aprovado!")
        else:
            print("Acesso negado!")