'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''


opcao = ''
total_gasto = 0
contador_prod = 0
menor = 0
cont = 0
nome_prod = ''
while opcao != 'N':
    nome = str(input('Digite o nome do produto: '))
    preco_prod = float(input('Digite o preço do produto R$: '))
    opcao = str(input('Quer continuar cadastrando mais produtos? [S/N]: ')).upper().strip()[0]
    total_gasto = total_gasto + preco_prod

    #Define o menor produto
    cont = cont + 1
    if cont == 1 or menor > preco_prod:
        menor = preco_prod
        nome_prod = nome
    else: 
        if preco_prod > 1000:
            contador_prod = contador_prod + 1
    
    
print(f'O total gasto é: R${total_gasto:.2f}\n{contador_prod} produto(s) com mais de R$1000 reais.\nE o produto mais barato é o {nome_prod} que custa R${menor:.2f}')