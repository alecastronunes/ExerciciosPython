from math import sin, cos, tan, radians
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
print('O ângulo de {} tem o COSENO de {:.2f}'.format(angulo, cosseno))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))