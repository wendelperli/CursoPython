lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um número: ')))
    r = str(input('Quer continuar? [ S / N ]')).upper()
    if r in 'N':
        break
print('-=' * 30)
print(f'A lista completa é {lista}')
for n in range(0, len(lista)):
    if lista[n] % 2 == 0:
        par.append(lista[n])

    if lista[n] % 2 == 1:
        impar.append(lista[n])
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
