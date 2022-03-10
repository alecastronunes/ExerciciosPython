from time import sleep
opcao = 0
while opcao != 5:
    n1 = int(input('Por favor, digite o primeiro valor: '))
    n2 = int(input('Por favor, digite o segundo valor: '))
    opcao = int(input('''ESCOLHA UMA DAS OPÇÕES ABAIXO: 
    [1] Somar.
    [2] Multiplicar.
    [3] Maior.
    [4] Novos Números.
    [5] Sair do Programa.
    Escolha: '''))
    if opcao == 1:
        resultado = n1 + n2
        print('O resultado da operação entre {} + {} é: {}'.format(n1, n2, resultado))
        sleep(2)
    elif opcao == 2:
        resultado = n1 * n2
        print('O resultado da operação entre {} X {} é: {}'.format(n1, n2, resultado))
        sleep(2)
    elif opcao == 3: 
        if n1 > n2:
            print('Entre {} e {}, o {} é o maior valor.'.format(n1, n2, n1))
            sleep(2)
        else:
            print('Entre {} e {}, o {} é o maior valor.'.format(n1, n2, n2))
            sleep(2)
    elif opcao == 4:
        opcao = 0
    elif opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5:
        print('OPERAÇÃO INVÁLIDA!!!')
        sleep(2)

print('FIM DO PROGRAMA!!!')