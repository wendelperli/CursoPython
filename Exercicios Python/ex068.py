from random import randint
print('=-'*40)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*40)
contv = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    soma = jogador + computador

    pi = str(input('Par ou Ímpar [P/I]: ')).upper().strip()[0]
    while pi not in 'PI':
        print('Digite apenas P ou I')
        pi = str(input('Par ou Ímpar [P/I]: ')).upper().strip()[0]
    print('-'*40)

    if soma % 2 == 0:
        print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU PAR')
        if pi == 'P':
            print('Você VENCEU')
            contv = contv + 1
        if pi == 'I':
            print('Você PERDEU!')
            break
    else:
        print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU ÍMPAR')
        if pi == 'P':
            print('Você PERDEU')
            break
        if pi == 'I':
            print('Você VENCEU!')
            contv = contv + 1
print('-'*40)

print('-='*40)
print(f'GAME OVER! Você venceu {contv} vezes.')