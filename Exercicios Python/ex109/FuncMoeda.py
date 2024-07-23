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

