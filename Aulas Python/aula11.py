print('\033[31mOlá, Mundo!')
print('\033[1;31;43mOlá, Mundo!')
print('\033[1;31;43mOlá, Mundo!\033[m')
print('\033[4;30;45mOlá, Mundo!\033[m')
print('\033[7;30mOlá, Mundo!\033[m')

nome = 'Guanabara'
print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format('\033[4;34m', nome, '\033[m'))

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}

print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format(cores['amarelo'], nome, cores['limpa']))
print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format(cores['pretoebranco'], nome, cores['limpa']))