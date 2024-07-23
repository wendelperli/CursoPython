import random
a1 = input(str('Primeiro Aluno: '))
a2 = input(str('Segundo Aluno: '))
a3 = input(str('Terceiro Aluno: '))
a4 = input(str('Quarto Aluno: '))
lista = [a1, a2, a3, a4]
sorteado = random.choice(lista)
print('O aluno escolhido foi {}'.format(sorteado))