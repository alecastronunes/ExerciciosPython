print('\033[1;34m='*10,'LOJAS ALEXANDRE', '='*10, '\033[m')
produto = float(input('\033[1;32mInforme o valor do produto: '))
print('''Escolha uma das formas de pagamento:
[1] - à vista dinheiro/cheque: 10%, de desconto
[2] - à vista no cartão: 5%, de desconto
[3] - em até 2x no cartão: preço formal
[4] - 3x ou mais no cartão: 20%, de juros''')
opcao = int(input('Qual das opções deseja escolher? '))
avista = produto - (0.1 * produto)
cartao = produto - (0.05 * produto)
juros = produto + (0.2 * produto)
if opcao == 1:
    print('Sua compra no valor de R${:.2f} reais vai custar R${:.2f} reais no final'.format(produto, avista))
elif opcao == 2:
    print('Sua compra no valor de R${:.2f} reais vai custar R${:.2f} reais no final'.format(produto, cartao))
elif opcao == 3: 
    prestacao = produto / 2
    print('Sua compra será parcelada em 2x de R${:.2f} reais.'.format(prestacao))
    print('Sua compra no valor de R${:.2f} reais, vai custar R${:.2f} reais no final.'.format(produto, produto))
elif opcao == 4:
    quantiParcelas = int(input('Quantas parcelas? '))
    qunatiPrestacao = (produto / quantiParcelas)
    valorParcelas = qunatiPrestacao + (0.2 * qunatiPrestacao)
    print('Sua compra será parcelada em {}x de R${:.2f} reais, com juros.'.format(quantiParcelas, valorParcelas))
    print('Sua compra no valor de R${:.2f} reais vai custar R${:.2f} reais no final'.format(produto, juros))
    #elif opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4:
else:
    print('\033[1;31mOPÇÃO INVÁLIDA de pagamento. Tente novamente.')
