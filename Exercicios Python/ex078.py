valores = []
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))

print(f'Você digitou os valores {valores}')
menor = valores[0]
maior = valores[0]
for cont in range(0, 5):
    if valores[cont] > maior:
        maior = valores[cont]
    if valores[cont] < menor:
        menor = valores[cont]
posmaior = []
posmenor = []

print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')