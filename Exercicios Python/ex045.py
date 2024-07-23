from random import randint
from time import sleep
print('Suas opções: ')
print('''
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogada = int(input('Qual é a sua jogada? '))

if jogada == 0:
    jogada = 'PEDRA'
elif jogada == 1:
    jogada = 'PAPEL'
elif jogada == 2:
    jogada = 'TESOURA'

else:
    print('JOGADA INVÁLIDA')

x = randint(0, 2)

if x == 0:
    pc = 'PEDRA'
elif x == 1:
    pc = 'PAPEL'
elif x == 2:
    pc = 'TESOURA'

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
sleep(0.5)
print('-='*20)

print('Jogador jogou {}'.format(jogada))
print('Computador jogou {}'.format(pc))

if jogada == pc:
    print('Deu empate!')
elif (jogada == 'PEDRA' and pc == 'TESOURA') or (jogada == 'PAPEL' and pc == 'PEDRA') or (jogada == 'TESOURA' and pc == 'PAPEL'):
    print('JOGADOR VENCE')

elif (pc == 'PEDRA' and jogada == 'TESOURA') or (pc == 'PAPEL' and jogada == 'PEDRA') or (pc == 'TESOURA' and jogada == 'PAPEL'):
    print('COMPUTADOR VENCE')

print('-='*20)