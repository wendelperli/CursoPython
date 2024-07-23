def aumentar(valor=0, taxa=0):
    aumentar = valor + (valor * (taxa/100))
    return aumentar

def diminuir(valor=0, taxa=0):
    diminuir = valor - (valor * (taxa/100))
    return diminuir

def dobro(valor=0):
    dobro = valor * 2
    return dobro

def metade(valor=0):
    metade = valor / 2
    return metade

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')

