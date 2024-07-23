#import math
#co = float(input('Comprimento do cateto oposto: '))
#ca = float(input('Comprimento do cateo adjascente: '))
#h = math.hypot(co, ca)
#print('A hipotenusa vai medir {:.2f}'.format(h))

co = float(input('Comprimento do cateo oposto: '))
ca = float(input('Comprimento do cateto adjascente: '))
h = (ca ** 2) + (co ** 2)
h = h ** (1 / 2)  # Número elevado a meia potência é a raiz quadrada
print('A hipotenusa vai medir {:.2f}'.format(h))
