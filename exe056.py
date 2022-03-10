media = 0
maiorm = 0
menorm = 0
quantidadeF = 0
nomevelho = ''
for pessoa in range(1, 5):
    print('='*10,'{}ª Pessoa'.format(pessoa),'='*10)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    media = idade + media
    mediaIdade = media /4
    if sexo == 'M':
        if idade > maiorm:
            maiorm = idade
            nomevelho = nome   
    if sexo == 'F':
        if idade < 20:
            menorm = idade
            quantidadeF += 1
print('A média de idade é: {} anos'.format(mediaIdade))
print('O homem mais velho tem: {} anos e se chama: {}'.format(maiorm, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(quantidadeF))