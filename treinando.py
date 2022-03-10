'''
n = 1
impar = 0
par = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
print('A quantidade de números pares digitados é: {} e a quantidade de número impares digitado é: {}'.format(par, impar))
print('FIM')'''

'''
n = 0
s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    else:
        s += n
#print(' A soma vale {}'.format(s))
print(f'A soma vale {s}')
'''

'''
nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
media = (nota_1 + nota_2) / 2
print(f'O resultado da média do exame é: {media}')
'''

'''
celsius = float(input('Digite um valor de temperatura em Celsius: '))
fahrenheit = (9/5) * celsius + 32
if fahrenheit > 90:
    print(f'A temperatura de {celsius}° graus, convertida em Fahrenheit é: {fahrenheit}. Está muito quente!!!')
elif fahrenheit < 30:
    print(f'A temperatura de {celsius}° graus, convertida em Fahrenheit é: {fahrenheit}. Está extremamente frio!!!')
else: 
    print(f'A temperatura de {celsius}° graus, convertida em Fahrenheit é: {fahrenheit}. Temperatura normal!!!')
'''
'''
invest_inicial = float(input('Informe o valor inicial: '))
taxa_anual = float(input('Informe a taxa anual: '))
invest_final = invest_inicial * (1 + taxa_anual)
print(f'O investimento final calculado será de: {invest_final:.2f}')
'''

'''
invest_inicial = float(input('Informe o valor inicial: '))
taxa = float(input('Informe a taxa anual: '))
taxa_porcentagem = (taxa / 100) * taxa 
taxa_anual = taxa_porcentagem * 120
invest_final = (invest_inicial * 120) + taxa_anual
print(f'O investimento final calculado será de: R${invest_final:.2f}')
'''
'''lanche = ['hamburger', 'suco', 'pizza', 'pudim']
lanche.append('cookie')
lanche.insert(0, 'cachorro-quente')
del lanche[3]
print(lanche[1])'''

'''
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista.')
'''
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista {a}')
print(f'Lista {b}')