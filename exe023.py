num = int(input('Digite um número de 0 a 999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('A Unidade do número é: {}'.format(u))
print('A Dezana do número é: {}'.format(d))
print('A Centena do número é: {}'.format(c))
print('O Milhar do número é: {}'.format(m))