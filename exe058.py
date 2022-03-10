from random import randint
numUsuario = '12'
numComputador = '14'
contador = 0
while numUsuario != numComputador:
    print('='*10, 'TENTE ADIVINHAR EM QUAL NÚMERO O COMPUTADOR ESTÁ PENSANDO!!!', '='*10)
    numUsuario = int(input('Digite um número entre 0 e 10: '))
    numComputador = randint(0, 10)
    if numUsuario > 10:
        print('Número inválido, tente novamente')
    else:
        contador = contador + 1
        if numUsuario == numComputador:
            print('Parabéns, você acertou! O número que o computador pensou foi: {}... e você precisou de {} tentativas'.format(numComputador, contador))
        else:
            print('Que pena, você errou, o número que o computador pensou foi: {}'.format(numComputador))
            