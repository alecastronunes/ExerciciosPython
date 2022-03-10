pesomaior = 0
pesomenor = 0
for c in range(1, 6):
    peso = float(input('Qual o peso da {}ª pessoa? '.format(c)))
    if c == 1:
        pesomaior = peso
        pesomenor = peso
    else:
        if peso > pesomaior:
            pesomaior = peso
        if peso < pesomenor:
            pesomenor = peso

print('O maior peso digitado foi: {}Kg'.format(pesomaior))
print('O menor peso digitado foi: {}Kg'.format(pesomenor))