while True:
    c = 0
    print('-' * 40)
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    while c <= 10:
        print(f'{n} x {c} = ', (n * c))
        c = c + 1
print('-'*40)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')