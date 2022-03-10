valores = []
while True:
    num = int(input('Digite um valor: '))
    if num in valores:
            print('O valor digitado já foi cadastrado, escolha outro!!!')
    else:
        valores.append(num)
    opcao = str(input('Quer continuar digitando valores? [S/N]: ')).upper().strip() [0]
    if opcao != 'S' and opcao != 'N':
        print('Opção inválida, escolha somente S ou N.')
    if opcao == 'N':
        valores.sort()
        print(f'Os valores cadastrados na lista são: {valores}')
        print('Fim do programa')
        break