from random import shuffle
a1 = input(str('Primeiro aluno: '))
a2 = input(str('Segundo aluno: '))
a3 = input(str('Terceiro aluno: '))
a4 = input(str('Quarto aluno: '))
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem de apresentação será: {} '.format(lista))
