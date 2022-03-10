distancia = float(input('Qual será a distância da sua viagem: '))
curta = 0.50 * distancia
longa = 0.45 * distancia
if(distancia <= 200):
    print('Sua viagem custará: R${:.2f} reais.'.format(curta))
else:
    print('Sua viagem custará: R${:.2f} reais.'.format(longa))