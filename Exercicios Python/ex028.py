import random
from time import sleep
print('-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--')
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--')
n = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(1)
r = random.randint(0, 5) # Gera um número aleatório entre 1 e 5
if (n >= 0) and (n <= 5) and (n == r):
    print('Você acertou! O número pensado foi {}'.format(n))
else:
    if (n >= 0) and (n <= 5) and (n != r):
        print('GANHEI! Eu pensei no número {} e não no {}!'.format(r, n))
    else:
        print('Programa encerrado. Você deveria ter digitado um número entre 0 e 5')



