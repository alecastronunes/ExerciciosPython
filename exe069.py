'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. '''


opcao = ''
cont_idade = 0
cont_sexo_masc = 0
cont_sexo_femi = 0
while opcao != 'N':
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Informe a idade da pessoa: '))
    sexo = str(input('Informe o sexo da pessoa: [F/M]: ')).upper().strip()[0]
    opcao = str(input('Deseja continuar cadastrando? [S/N]: ')).upper().strip()[0]
    
    if idade > 18:
        cont_idade = cont_idade + 1
    if sexo == 'M':
        cont_sexo_masc = cont_sexo_masc + 1
    if sexo == 'F' and idade < 20:
        cont_sexo_femi = cont_sexo_femi + 1
print(f'A quantidade de pessoas acima de 18 anos é: {cont_idade}\nForam cadastradas {cont_sexo_masc} pessoas do sexo masculino.\nForam cadastradas {cont_sexo_femi} pessoas do sexo feminio com menos de 20 anos.')