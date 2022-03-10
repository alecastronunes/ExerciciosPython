import requests
from tkinter import *
from random import sample

def gerar_senha():
    caracteres = 'abcdefghijklmnopqrstuvwxyz01234567890!@#$%&*'
    print('='*10, '\033[1;4;31mGERADOR DE SENHA\033[m', '='*10)
    tamanho = int(input('Informe quantos caracteres a senha deve ter: '))
    senha = ''.join(sample(caracteres, tamanho))
    #if(tamanho < 8 or tamanho > 12 ):
        #print('Sua senha deve conter no mínimo 8 e no máximo 12 caracteres')
    #else:
       # print('A senha gerada foi: {}'.format(senha))
    
    texto_cotacoes['text'] = f'''Senha: {senha}'''
janela = Tk()
janela.title('Gerador de Senha')
janela.geometry('400x400')

texto_orientacao = Label(janela, text='Clique no botão para gerar a senha.')
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text='Gerar Senha.', command=gerar_senha)
botao.grid(column=0, row=1, padx=10, pady=10)

texto_cotacoes = Label(janela, text='')
texto_cotacoes.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()