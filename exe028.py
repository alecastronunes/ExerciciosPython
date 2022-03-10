from random import randint
print('='*10, 'TENTE ADIVINHAR EM QUAL NÚMERO O COMPUTADOR ESTÁ PENSANDO!!!', '='*10)
numUsuario = int(input('Digite um número entre 0 e 5: '))
numComputador = randint(0, 5)
if numComputador == numUsuario:
    print('\033[1;34mParabéns, você acertou, o número que o computador pensou foi: {}\033[m'.format(numComputador))

else:
    print('\033[1;31mQue pena, você errou, o número que o computador pensou foi: {}\033[m'.format(numComputador))
