c = q = m = s = 0
r = 'S'
while r == 'S':
    n = int(input('Digite um número: '))
    while c == 0:
        maior = n
        menor = n
        c = c + 1
    if n >= maior:
        maior = n
    if n <= menor:
        menor = n
    q = q + 1
    s = s + n
    r = str(input('Quer continuar? [ S / N ]')).upper().strip()[0]
m = s / q
print('Você digitou {} números e a média foi {}'.format(q, m))
print('O maior número digitado foi {} e o menor foi {}'.format(maior, menor))
