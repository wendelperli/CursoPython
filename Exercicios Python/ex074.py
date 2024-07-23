from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)) # Sorteia 5 número entre 1 e 10
print(numeros)

print('Os valores sorteadors foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
    
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
