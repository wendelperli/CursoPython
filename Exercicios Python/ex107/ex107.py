# Programa Principal
import FuncMoeda
preco = float(input('Digite o preço: R$'))
taxa = float(input('Qual é a taxa? '))
print(f'A metade de R${preco} é R${FuncMoeda.metade(preco)}')
print(f'O dobro de R${preco} é R${FuncMoeda.dobro(preco)}')
print(f'Aumentando {taxa}%, temos R$ {FuncMoeda.aumentar(preco, taxa)}')
