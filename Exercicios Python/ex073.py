tabela = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',
          'Flamengo', 'Vasco da Gama', 'Chapecoense', 'Atlético', 'Botafogo',
          'Atlético-PR', 'Bahia', 'São Paulo', 'Fliminense', 'Sport Recife',
          'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('-=' * 30)
print(f'Lista de times do Brasileirão: {tabela}')
print('-=' * 30)
print(f'Os 5 primeiros são: {tabela[0:6]}')
print('-=' * 30)
print(f'Os 4 últimos são: {tabela[-4:]}')
print('-=' * 30)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('-=' * 30)
print(f'O Chapecoense está {tabela.index("Chapecoense")+1}ª posição')
