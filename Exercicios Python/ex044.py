print('{:=^40}'.format(' LOJAS GUANABARA '))
preco = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[1] à vista dinheiro/cheque (10% de desconto)')
print('[2] à vista cartão (5% de desconto)')
print('[3] 2x no cartão (Preço normal')
print('[4] 3x ou mais no cartão (20% de juros)')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    final = preco - ((10 /100) * preco)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, final))
elif opcao == 2:
    final = preco - ((5 / 100) * preco)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, final))
elif opcao == 3:
    final = preco / 2
    print('Sua compra será parcelada em 2x vezes de R${:.2f} SEM JUROS'.format(final))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, preco))
elif opcao == 4:
    vezes = int(input('Em quantas vezes vai parcelar? '))
    if vezes >= 3:
        final = preco + ((20 /100) * preco)
        parcela = final / vezes
        print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(vezes, parcela))
        print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, final))
    elif vezes < 3:
        print('Você deve digitar uma parcela de 3 vezes ou mais nessa opção. Comece novamente.')
else:
    final = preco
    print('Opção inválida de pagamento. Tente novamente')
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, final))
