'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

resposta = 0
acumulador = 0
soma = 0
media = 0
maior = 0
menor = 0
while resposta != 5:
    numero = int(input('Digite um número: '))
    resposta = int(input('''Quer continuar digitando mais números? 
    [0] Sim
    [5] Não \n opção: '''))
    acumulador = acumulador + 1
    soma = soma + numero
    media = soma / acumulador

    #Verificar o maior e o menor número digitado
    if acumulador == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
             menor = numero

#print('O acumulador tem: {} números.'.format(acumulador))
print(' A media entre todos os valores digitados é: {:.2f} \n O maior valor digitado foi: {} \n O menor valor digitado foi: {}'.format(media, maior, menor))