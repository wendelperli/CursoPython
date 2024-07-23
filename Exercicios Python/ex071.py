print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
valor = int(input('Que valor você quer sacar? R$'))

if valor % 50 < 50:
    resto50 = valor % 50
    resul50 = valor // 50
    if resul50 != 0:
        print(f'Total de {resul50} cédulas de R$50')

if resto50 % 20 < 20:
    resto20 = resto50 % 20
    resul20 = resto50 // 20
    if resul20 != 0:
        print(f'Total de {resul20} cédulas de R$20')

if resto20 % 10 < 10:
    resto10 = resto20 % 20
    resul10 = resto20 // 10
    if resul10 != 0:
        print(f'Total de {resul10} cédulas de R$10')

if resto10 % 10 < 10:
    resto1 = resto10 % 10
    if resto1 != 0:
        print(f'Total de {resto1} cédulas de R$1')
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
'''
# Solução Guanabara

print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
'''