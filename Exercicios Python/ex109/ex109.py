# Programa Principal
import FuncMoeda
preco = float(input('Digite o preço: R$'))
taxa = float(input('Qual é a taxa? '))
print(f'A metade de {FuncMoeda.moeda(preco)} é {(FuncMoeda.metade(preco, True))}')
print(f'O dobro de {FuncMoeda.moeda(preco)} é {(FuncMoeda.dobro(preco, True))}')
print(f'Aumentando {taxa}%, temos {(FuncMoeda.aumentar(preco, taxa, True))}')
print(f'Reduzindo 13%, temos {FuncMoeda.diminuir(preco, 13, True)}')
