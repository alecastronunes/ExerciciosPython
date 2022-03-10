numero = int(input('Você quer saber a tabuada de qual número: '))
contador = 0
for c in range(0, 10+1):
    resultado = numero * c
    print('{} X {} = {}'.format(numero, c , resultado))