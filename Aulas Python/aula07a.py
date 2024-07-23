n1 = int(input('Digite um número: '))
n2 = int(input('Digite ouuto número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma dos números é {}, \n o produto é {} e a \n divisão é {:.3f}'.format(s, m, d), end ='')
print(' Divisão inteira {} e potência {}'.format(di, e))
