from time import sleep
soma = 0
contador = 0
print('-' * 39)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 39)
precos = (0, 1.75, 2.00, 15.90, 25.00, 4.20, 9.99, 120.32, 22.30, 34.90)

produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
for produto in range(0, len(produtos)):
    if produto % 2 == 0:
        contador = contador + 1
        print(f'Opção: {contador} - {produtos[produto]:.<30}', end='')
    else:
        print(f'R${produtos[produto]:>7.2f}')
print('-' * 39)

while True:
    opcao = int(input('Escolha uma das opções da lista de compras: '))
    if opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4 or opcao == 5 or opcao == 6 or opcao == 7 or opcao == 8 or opcao == 9:
        soma  = soma + precos[opcao]
    if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5 and opcao != 6 and opcao != 7 and opcao != 8 and opcao != 9:
        print('Opção inválida!')
    decisao = str(input('Deseja continuar comprando [S/N]?: ')).upper().strip()[0]
    while decisao != 'S' and decisao != 'N':
        print('Opção inválida!!! Digite somente S ou N.')
        sleep(2)
        decisao = str(input('Deseja continuar comprando [S/N]?: ')).upper().strip()[0]
    if decisao == 'N':
        break
print(f'O valor total da compra é: R${soma:.2f}')