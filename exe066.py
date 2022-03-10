acumulador = 0
soma = 0
while True:
    numero = int(input('Digite um número inteiro (999 para parar): '))
    if numero == 999:
        break
    else:
        soma += numero
        acumulador += 1
print(f'Foram digitados {acumulador} números e a soma entre eles é: {soma}')