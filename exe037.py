numero = int(input('Digite um número inteiro: '))
print('''\033[1;32mEscolha uma das bases para conversão:\033[m
\033[1;31m[1]\033[m Converter para BINÁTIO
\033[1;31m[2]\033[m Converter para OCTAL
\033[1;31m[3]\033[m Converter para HEXADECIMAL''')
opcao = int(input('\033[1;32mQual sua opção? \033[m'))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a: {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a: {}'.format(numero, oct(numero))[2:])
elif opcao == 3:
    print('{} convertido para HEXADECIAMAL é igual a: {}'.format(numero, hex(numero))[2:])
elif opcao != 1 or 2 or 3:
    print('Opção inválida, por favor, tente novamente!!!')
