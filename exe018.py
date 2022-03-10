import random
print('='*10,'QUEM VAI LAVAR A LOUÇA????', '='*10)
n1 = input('Digite o primeiro nome: ')
n2 = input('Digite o segundo nome: ')
n3 = input('Digite o terceiro nome: ')
#n4 = input('Digite o quarto nome: ')
lista = [n1, n2, n3]
resultado = random.choice(lista)
print('A pessoa escolhida para lava a louça foi: {}'.format(resultado))