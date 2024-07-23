print('-' * 25)
print('LOJA SUPER BARATÃO')
print('-' * 25)
total = 0
maisdemil = 0
maisbarato = 0
produtomaisbarato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço R$ '))
    if maisbarato == 0:
        maisbarato = preco
    if preco < maisbarato:
        maisbarato = preco
        produtomaisbarato = produto
    total = total + preco
    if preco > 1000:
        maisdemil = maisdemil + 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [ S / N ] ')).strip().upper()[0]
    if resp == 'N':
        break

print('-' * 25, 'FIM DO PROGRAMA', '-' * 25)
print(f'O total da compra foi R${total}')
print(f'Temos {maisdemil} prosuto custando mais de R$1000')
print(f'O produto mais barato foi {produtomaisbarato} que custa R${maisbarato}')
