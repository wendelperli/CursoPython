# Programa Principal
from utilidadescev import moeda
preco = float(input('Digite o preço: R$'))
taxa = float(input('Qual é a taxa? '))
moeda.resumo(preco, taxa, 20)
