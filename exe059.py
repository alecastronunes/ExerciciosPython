sair = 0
opcao = 0
while opcao != 5:
    opcao = int(input('''ESCOLHA UMA DAS OPÇÕES ABAIXO: 
[1] Somar.
[2] Multiplicar.
[3] Maior.
[4] Novos Números.
[5] Sair do Programa.
Escolha: '''))
    
    if opcao == 1:
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
        resultado = n1 + n2
        print('O resultado da operação foi {}'.format(resultado))
    elif opcao == 2:
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
        resultado = n1 * n2
        print('O resultado da operação foi {}'.format(resultado))
    elif opcao == 3:
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
        if n1 > n2:
            print('{} é o maior entre os valores comparados'.format(n1))
        else:
            print('{} é o maior entre os valores comparados.'.format(n2))
    elif opcao == 4:
        opcao = int(input('''ESCOLHA UMA DAS OPÇÕES ABAIXO: 
        [1] Somar.
        [2] Multiplicar.
        [3] Maior.
        [4] Novos Números.
        [5] Sair do Programa.
        Escolha: '''))
    if opcao == 1:
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
        resultado = n1 + n2
        print('O resultado da operação foi {}'.format(resultado))
    elif opcao == 2:
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
        resultado = n1 * n2
        print('O resultado da operação foi {}'.format(resultado))
    elif opcao == 3:
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
        if n1 > n2:
            print('{} é o maior entre os valores comparados'.format(n1))
        else:
            print('{} é o maior entre os valores comparados.'.format(n2))
        
    
print('FIM DO PROGRAMA')