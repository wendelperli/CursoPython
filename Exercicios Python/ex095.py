jogador = {}
time = []

while True:
    jogador.clear()
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
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-' * 40)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999) para parar '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
        print('-' * 34)
print('<< VOLTE SEMPRE >>')
