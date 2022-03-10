from random import shuffle
n1 = input('Digite o primeiro nome: ')
n2 = input('Digite o segundo nome: ')
n3 = input('Digite o terceiro nome: ')
#n4 = input('Digite o quarto nome: ')
semana = [' SEGUNDA', ' TERÇA', ' QUARTA', ' QUINTA', ' SEXTA', ' SÁBADO']
lista = [n1, n2, n3, n1, n2, n3]
shuffle(lista)
print('\033[1;31;47m='*10, 'A ordem para lavar a louça é: ', '='*10, '\033[m')
print(semana)
print(lista)
