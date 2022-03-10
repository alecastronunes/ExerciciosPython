nome = input('Digite um nome completo: ').strip()
res = nome.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é: {}'.format(res[0]))
print('Seu último nome é: {}'.format(res[len(res)-1]))

   