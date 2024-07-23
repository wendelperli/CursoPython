n = int(input('Digite um número para ver sua tabuada: '))
print('==================')
for c in range(0, 11):
    r = n * c
    print(n, 'x', c, '=', r)

#n = int(input('Digite um número para ver sua tabuada: '))
#for c in range(0, 11):
#    print('{} x {:2} = {}'.format(n, c , n * c))