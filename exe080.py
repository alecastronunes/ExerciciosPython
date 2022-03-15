lista = []
for c in range (0, 5):
    valores = int(input('Digite um valor: '))
    if c == 0 or valores > lista[-1]:
        lista.append(valores)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if valores <= lista[pos]:
                lista.insert(pos, valores)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print('-='*30)
print(f'Os valores digitados em ordem foram {lista}')