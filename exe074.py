'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''

from random import randint
maior = 0
menor = 0
print('A listagem de números gerados é: ', end='')
for c in range(1, 6):
    numeros = (randint(0, 100))
    print(numeros,'',end='')
    
    #Este bloco de código define o maior e o menor número.
    if c == 1:
        maior = numeros
        menor = numeros
    else:
        if numeros > maior:
            maior = numeros
        elif numeros < menor:
            menor = numeros
print(f'\nO maior valor gerado foi: {maior}')
print(f'O menor valor gerado foi: {menor}')