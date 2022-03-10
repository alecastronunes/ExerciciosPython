r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print('Os seguimentos acima pordem formar um triângulo! ', end='')
    if r1 == r2 and r2 == r3:
        print('EQUILATERO!')

    if r1 == r2 or r2 == r3 or r3 == r1:
        print('ISÓSCELES!')

    if r1 != r2 and r2 != r3 and r3 != r1:
        print('ESCALENO!')
else: 
    print('Os seguimentos não podem formar um triângulo!')
