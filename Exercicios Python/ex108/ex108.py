# Programa Principal
import FuncMoeda
preco = float(input('Digite o preço: R$'))
taxa = float(input('Qual é a taxa? '))
print(f'A metade de {FuncMoeda.moeda(preco)} é {FuncMoeda.moeda(FuncMoeda.metade(preco))}')
print(f'O dobro de {FuncMoeda.moeda(preco)} é {FuncMoeda.moeda(FuncMoeda.dobro(preco))}')
print(f'Aumentando {taxa}%, temos {FuncMoeda.moeda(FuncMoeda.aumentar(preco, taxa))}')
