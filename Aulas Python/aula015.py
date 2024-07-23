'''cont = 1
while cont <= 10:
    print(cont, '-> ', end='')
    cont += 1
print('Acabou')'''
'''n = s =0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
#print('A soma vale {}'.format(s))
print(f'A soma vale {s}')'''
nome = 'José'
idade = 33
salário = 987.3
print(f'O {nome} tem {idade} anos.')  # Python 3.6+
print('O {} tem {} anos.'.format(nome, idade))  # Python 3
print('O %s tem %d anos.' % (nome, idade))  # Python 2
print(f'O {nome} tem {idade} anos e ganha R${salário:.2f}.')
