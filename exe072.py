'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if n > 20 or n < 0:
        print('Opção inválida, tente novamente!!!')
    else:
        print(f'Você digitou o número {numero[n]}')
        break