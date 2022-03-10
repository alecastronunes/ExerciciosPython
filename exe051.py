termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite  a razão da PA: '))
decimo = termo + (10 - 1) * razao
if razao <= 1:
    print('O número digitado é inválido. Digite um número a partir de 1')
else:
    for c in range(termo, decimo + razao, razao):
        print('{} '.format(c), end='-> ')
print('FIM')