'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)'''

contador = 0
numero = 0
resultado = 0
while numero != 999:
    numero = int(input('Digite um número inteiro: '))
    contador = contador + 1
    resultado = resultado + numero
    print(numero)
print('Foram digitados {} números e a soma de todos os números digitados é: {}.'.format(contador-1, resultado-numero))
