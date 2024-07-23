soma = 0
imv = 0
mcmv = 0
for c in range(1, 5):
    print('-' * 5, '{}ª PESSOA'.format(c), '-' * 5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    soma = soma + idade
    sexo = str(input('Sexo [M / F]: ')).strip()
    if idade > imv and sexo in 'Mm':
        imv = idade
        hmv = nome

    if sexo in 'Ff' and idade < 20:
        mcmv = mcmv + 1
media = soma / 4
print('A média de idade do grupo é de {} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(imv, hmv))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mcmv))
