from random import randint
contador = 0
while True:
    numero = int(input('Digite um número: '))
    opcao = str(input('Par ou Ímpar [P/I]: ')).upper().strip()[0]
    computador = randint(0, numero)
    soma = numero + computador
    if opcao != 'P' and opcao != 'I':
            print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE!!!')
    if opcao == 'P':
        if soma % 2 == 0:
            contador += 1
            print('-' * 30)
            print(f'Você jogou {numero} e o computador jogou {computador}. Total de {soma} deu PAR')
            print('-' * 30)
            print('VOCÊ GANHOU!!!')
        elif opcao == 'P':
            if soma % 2 != 0:
                print(f'Você jogou {numero} e o computador jogou {computador}. Total de {soma} deu ÍMPAR')
                print(f'GAME OVER!!!... Você venceu só {contador} vezes')
                break
    elif opcao == 'I':
        if soma % 2 == 0:
            print('-' * 30)
            print(f'Você jogou {numero} e o computador jogou {computador}. Total de {soma} deu PAR')
            print('-' * 30)
            print(f'GAME OVER!!!... Você venceu só {contador} vezes')
            break
        elif opcao == 'I':
            if soma != 0:
                contador += 1
                print(f'Você jogou {numero} e o computador jogou {computador}. Total de {soma} deu ÍMPAR')
                print('VOCÊ GANHOU!!!')
        
                                
