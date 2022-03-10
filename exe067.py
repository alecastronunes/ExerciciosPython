contador = 0
acumulador = 0
while True:
    numero = int(input('Quer saber a tabuada de qual número: '))
    print('-' * 30)
    if numero == numero < 0:
        break
    else:
        for contador in range(1, 10-1):
            acumulador += 1
            multiplicao = numero * acumulador
            print(f'{numero} X {acumulador} = {multiplicao}')
    print('-' * 30)
print('Fim') 