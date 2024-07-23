# Programa Principal
from utilidadescev import dado
from utilidadescev import moeda
preco = dado.leiaDinheiro('Digite o preço: R$ ')
taxa = float(input('Qual é a taxa? '))
moeda.resumo(preco, taxa, 20)
