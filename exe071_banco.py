'''
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print('=' * 30)
print('{:^30}'.format('SAQUE JÁ'))
print('=' * 30)

valor_saque = int(input('Qual o valor a ser sacado? R$: '))
total = valor_saque
cedula_maior = 50
total_cedula = 0

#Subtraindo do valor total digitado até zerar
while True:
    if total >= cedula_maior:
        total = total - cedula_maior
        total_cedula = total_cedula + 1
    else: 
        if total_cedula > 0:
            print(f'Total de {total_cedula:.2f} cédulas de R$ {cedula_maior}')
        if cedula_maior == 50:
            cedula_maior = 20
        elif cedula_maior == 20:
            cedula_maior = 10
        elif cedula_maior == 10:
            cedula_maior = 1
        total_cedula = 0
        if total == 0:
            break
print('Volte sempre ao Banco SAQUE JÁ! Tenha um bom dia!')