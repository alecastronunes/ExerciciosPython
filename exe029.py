veloCarro = int(input('Informe a velocidade do carro: '))
multa = (veloCarro - 80) * 7 
if veloCarro > 80:
    print('Você excedeu o limite permitido que pe de 80km/h, portanto, o valor da multa será de: R${:.2f} reais.'.format(multa))
else:
    print('Velocidade dentro dos limites permitidos!!!')