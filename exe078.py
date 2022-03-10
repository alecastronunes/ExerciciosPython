numeros = []
maior = 0
menor = 0
for c in range(0, 5):
    n = int(input(f'Digite um valor para a posição {c}: '))
    numeros.append(n)
    if c == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
print('=' * 35)
#Verifica as posições do maior e menor número.
print(f'O maior valor digitado foi: {maior}, na posição ', end='')
for i, v in enumerate(numeros):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado fo: {menor}, posição ', end='')
for i, v in enumerate(numeros):
    if v == menor:
        print(f'{i}... ', end='')
print()