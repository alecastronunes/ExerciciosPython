n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

#verifica qual é o maior valor
maior = n2
if n1 > n2 and n2 > n3:
    maior = n1
if n3 > n2 and n3 > n1:
    maior = n3
print('O maior valor digitado foi {}'.format(maior))

#verifica qual o menor valor
menor = n2
if n1 < n2 and n2 < n3:
    menor = n1
if n3 < n1 and n3 < n2:
    menor = n3
print('O menor valor digitado foi {}'.format(menor))