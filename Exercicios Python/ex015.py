da = int(input('Quantos dias alugados? '))
km = float((input('Quantos Km rodados? ')))
total = (60 * da) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(total))