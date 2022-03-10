'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

valores = (int(input('Digite um número: ')), int(input('Digite um númro: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))
print(f'Você digitou os valores: {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes.')
if 3 not in valores:
    print('O valor 3 não está em nenhum posição.')
else:
    print(f'O primeiro valor 3 foi digitado na {valores.index(3)+1}ª posição')
    print('Os valores pares digitados foram: ', end='')
for valor in valores:
    if valor % 2 == 0:
        print(valor, end=' ')