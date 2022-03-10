n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('O maior valor é: {}'.format(n1))
if n2 > n1:
    print('O maior valor é: {}'.format(n2))
elif n1 == n2:
    print('Os valores digitados são iguais')