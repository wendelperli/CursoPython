jogador = {'nome': str(input('Nome do jogador: '))}
npartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
lista = []
soma = 0
for c in range(0, npartidas):
    ngols = int(input(f'Quantos gols na partida {c}: '))
    lista.append(ngols)
    jogador['gols'] = lista[:]
for c in range(0, len(lista)):
    soma = soma + lista[c]
jogador['total'] = soma
print('-=' * 50)
print(jogador)
print('-=' * 40)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 40)
print(f'O jogador {jogador["nome"]} jogou {npartidas} partidas')
for c in range(0, npartidas):
    print(f'=> Na partida {c}, fez {lista[c]} gols.')
print(f'Foi um total de {soma} gols')
print('-=' * 40)
