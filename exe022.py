nomeCompleto = input('Digite seu nome completo: ')
resmaiusculo = nomeCompleto.upper()
resminusculo = nomeCompleto.lower()
quantidadeletras = nomeCompleto.__len__()
quantidadenome = nomeCompleto.split()
#resultquantnome = quantidadenome.__len__()
print('Seu nome em maiúsculo é: {}'.format(resmaiusculo))
print('Seu nome em minúsculo é: {}'.format(resminusculo))
print('A quantidade de letras que seu nome tem é: {}'.format(quantidadeletras))
print('A quantidade de letras do seu primeiro nome é: {}'.format(len((quantidadenome[0]))))