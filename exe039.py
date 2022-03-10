from datetime import date
anoNascimento = int(input('Informe seu ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNascimento
falta = 18 - idade
passou = idade - 18
if idade < 18:
    print('Ainda não chegou sua hora, você tem {} anos, ainda falta {} anos para o seu alistamento.'.format(idade, falta))
elif idade == 18:
    print('Chegou sua hora de se alistar, você tem {} anos.'.format(idade))
else:
    print('Você passou {} anos do serviço militar obrigatório... ALISTE-SE!!!'.format(passou))
