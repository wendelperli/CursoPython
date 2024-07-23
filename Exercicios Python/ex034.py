s = float(input('Qual é o salário do funcionário? R$'))
if s > 1250.00:
    ns = ((10 / 100) * s) + s
else:
    ns = ((15 /100) * s) + s
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(s, ns))
