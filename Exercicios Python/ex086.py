'''matriz = [[], [], []]
for cont2 in range(0, 3):
    matriz[0].append(int(input(f'Digite um valor para [0, {cont2}]: ')))
for cont3 in range(0, 3):
    matriz[1].append(int(input(f'Digite um valor para [1, {cont3}]: ')))
for cont4 in range(0, 3):
    matriz[2].append(int(input(f'Digite um valor para [2, {cont4}]: ')))
print(matriz[0])
print(matriz[1])
print(matriz[2])'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
