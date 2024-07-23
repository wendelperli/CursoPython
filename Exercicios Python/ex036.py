vc = float(input('Qual é o valor da casa: R$'))
sal = float(input('Qual é o salário do comprador: R$?'))
af = int(input('Quantos anos de financiamento?'))

pmensal = vc / (af * 12)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(vc, af, pmensal))
minimo = (30/100) * sal
if pmensal <= minimo:
    print('Empréstimo APROVADO!')
else:
    print('Empréstimo NEGADO')
