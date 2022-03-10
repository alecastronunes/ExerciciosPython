from math import hypot
catetoOpo = float(input('Digite o valor do cateto oposto: '))
catetoAdj = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = hypot(catetoOpo, catetoAdj)
print('A hipotenusa vai medir: {:.2f}'.format(hipotenusa))
#hipotenusa = (catetoOpo ** 2 + catetoAdj ** 2) ** (1/2)
#print('O comprimento da hipotenusa é: {}'.format(hipotenusa))