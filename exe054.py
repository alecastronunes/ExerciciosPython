from datetime import date
contMenor = 0
contMaior = 0
for c in range(1, 8):
    anoAtual = date.today().year
    ano = int(input('Em que ano a {}ª nasceu? '.format(c)))
    idade = anoAtual - ano
    if idade < 21:
        contMenor = contMenor + 1
    else:
        contMaior = contMaior + 1
print('Ao todo tivemos {} pessoas menores de idade.'.format(contMenor ))
print('E também tivemos {} pessoas maiores de idade.'.format(contMaior))
