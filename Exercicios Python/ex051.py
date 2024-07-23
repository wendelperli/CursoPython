print('='*25)
print('10 TERMOS DE UMA PA')
print('='*25)
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
for c in range(1, 11):
    print(n, end=' -> ')
    n = n + r
print('ACABOU!')

'''primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 -1) * razão
for c in range(primeiro, décimo + razão, razão):
    print('{} '.format(c), end=' -> ')
print('ACABOU!')'''