valores = []
while True:
    n = (int(input('Digite um valor: ')))
    if n not in valores:
         valores.append(n)
         print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')

    resposta = str(input('Quer continuar? [ S / N ]')).upper()
    if resposta in 'N':
        break
print('-=' * 30)
print(f'Você digitou os valores {sorted(valores)}')
