'''from math import factorial
numero = int(input('Digite um número para calcular seu fatorial: '))
fatorial = factorial(numero)
print('O fatorial de {} é {}'.format(numero, fatorial))'''

numero = int(input('Digite um número para calcular seu fatorial: '))
contador = numero
fatorial = 1
print('Calculando o fatorial de {}!'.format(numero))
while contador > 0:
    print('{}, '.format(contador), end='')
    fatorial = fatorial * contador
    contador = contador - 1
print('é = {}'.format(fatorial))