from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
#copcao = int(input('Qual é sua opção? '))
opcao = 0
while opcao != 5:
    print('=-=' * 15)
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos números')
    print('[5] sair do programa')
    opcao = int(input('>>>>>Qual é sua opção? '))

    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))

    elif opcao == 2:
        multiplicacao = n1 * n2
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, multiplicacao))

    elif opcao == 3:
        if n1 > n2:
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, n1))
        if n2 > n1:
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, n2))

    elif opcao == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))

    elif opcao == 5:
        print('PROGRAMA FINALIZADO!')

    else:
        print('Opção inválida, tente novamente')
        sleep(1)
print('=-='*15)
