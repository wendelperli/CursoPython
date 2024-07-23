d = float(input('Qual é a distância da sua viagem? '))
if d <= 200:
    p = (d * 0.50)
else:
    p = (d * 0.45)
print('Você está prestes a começar uma viagem de {:.1f}Km'.format(d))
print('O preço da sua passagem será de R${:.2f}'.format(p))
