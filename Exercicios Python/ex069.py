totp = 0
toth = 0
totm = 0

while True:
    print('-' * 25)
    print('CADASTRE UMA PESSOA')
    print('-' * 25)

    idade = int(input('Idade: '))
    if idade >= 18:
        totp = totp + 1

    sexo = str(input('Sexo: ')).strip().upper()[0]
    while sexo not in 'FM':
        print('Digite apenas F ou M')
        sexo = str(input('Sexo: ')).strip().upper()[0]
    if sexo == 'M':
        toth = toth + 1
    if sexo == 'F' and idade < 20:
        totm = totm + 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [ S / N ]')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {totp}.')
print(f'Ao todo temos {toth} homens cadastrados.')

print(f'E temos {totm} mulheres com menos de 20 anos.')
print('Acabou!')