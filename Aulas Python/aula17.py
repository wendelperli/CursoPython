''''#num = (2, 5, 9, 1)
#print(num)

num = [2, 5, 9, 1]
num[2] = 3
num.append(7) # Adiciona o valor 7 ao final da lista
num.sort() # Coloca em ordem
num.sort(reverse=True) # Coloca em ordem reversa
#num.insert(2, 0) # Isere o valor 0 na poisção 2
num.insert(2, 2)
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 4')
# num.pop() # Remove o último valor da lista
#num.pop(2) # Remove o valor da posição 2
# num.remove(2) # Remove o valor do índice (apenas a primeira ocorrência)
print(num)
print(f'Essa lista tem {len(num)} elementos') # Mostra quantos elementos tem na lista '''

'''valores = [] # Cria lista vazia
valores.append(5) # Insere valor
valores.append(9) # Insere valor
valores.append(4) # Insere valor
print(valores) #

for v in valores:
    print(f'{v}...')

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')'''

'''valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')'''

'''# Ligação entre duas listas
a = [2, 3, 4, 7]
b = a
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')'''

a = [2, 3, 4, 7]
b = a[:] # Pega todos os valores de A e COPIA para B (Manda B receber todos os items de A)
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')