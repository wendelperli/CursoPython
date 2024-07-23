'''from time import sleep
valores = []

def maior(*v):
    print('-=' * 30)
    while True:
        valores.append(int(input('Digite um valor: ')))
        resp = str(input('Quer continuar? [S /N]')).upper()[0]
        if resp == 'N':
            break
    print('Analisando os valores passados...')
    for c in range(0, len(valores)):
        print(valores[c], end=' ')
        sleep(0.4)
    print(f'Foram informados {len(valores)} valores ao todo.')
    print(f'O maior valor informado foi {max(valores)}')
    print('-=' * 30)

maior(valores)'''

# SOLUÇÃO GUANABARA
from time import sleep

def maior(*num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


# Programa principal

maior(2, 9, 4, 5, 7, 1)
maior(2, 7, 0)
maior(1, 2)
maior()
