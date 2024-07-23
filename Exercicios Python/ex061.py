print('Gerador de PA')
print('-='*15)
n = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
c = 1
while c <= 10:
    print(n, '-> ', end='')
    n = n + r
    c = c + 1
print('FIM')
