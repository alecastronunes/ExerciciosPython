valorCasa = float(input('Qual o valor da casa: R$ '))
salario = float(input('Quanto você ganha: R$ '))
anos = int(input('Em quantos anos você quer pagar a casa: '))
parcela = valorCasa / (anos * 12)
porcentagem = (30 / 100) * salario
if parcela > porcentagem:
    print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}. EMPRÉSTIMO NEGADO'.format(valorCasa, anos, parcela), end='') 
else:
    print('Empréstimo aprovado com sucesso!!!')
    print('A prestação será de: {:.2f}'.format(parcela))

