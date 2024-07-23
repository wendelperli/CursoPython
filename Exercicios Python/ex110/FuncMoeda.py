def aumentar(valor=0, taxa=0, formato=False):
    aumentar = valor + (valor * (taxa/100))
    return aumentar if formato is False else moeda(aumentar)

def diminuir(valor=0, taxa=0, formato=False):
    diminuir = valor - (valor * (taxa/100))
    return diminuir if formato is False else moeda(diminuir)

def dobro(valor=0, formato=False):
    dobro = valor * 2
    return dobro if not formato else moeda(dobro)

def metade(valor=0, formato=False):
    metade = valor / 2
    return metade if not formato else moeda(metade)

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')

def resumo(preco=0, taxa=10, taxar=5):
    print('-' * 40)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 40)
    print(f'Preço analisado: \t {moeda(preco)}')
    print(f'Metade do preço: \t {moeda(preco)} é {metade(preco, True)}')
    print(f'Dobro do preço: \t {moeda(preco)} é {dobro(preco, True)}')
    print(f'{taxa}% de aumento: \t {aumentar(preco, taxa, True)}')
    print(f'{taxar}%de redução: \t\t {diminuir(preco, taxar, True)}')
    print('-' * 40)
