v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
v3 = int(input('Digite o terceiro valor: '))
menor = v1
maior = v1
if v1 < menor:
    menor = v1
if v2 < menor:
        menor = v2
if v3 < menor:
        menor = v3

if v1 > maior:
    maior = v1
if v2 > maior:
    maior = v2
if v3 > maior:
    maior = v3

print('O menor valor digitado foi {}'.format(menor))
print('O menor valor digitado foi {}'.format(maior))
