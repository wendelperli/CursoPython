from math import sin, cos, tan, radians
a = float(input('Digite o ângulo que você deseja: '))
print('O ângulo de {:.2f} tem o SENO de {:.2f}'.format(a, sin(radians(a)))) #Transforma o sin que está em graus em radianos
print('O ângulo de {:.2f} tem o COSSENO de {:.2f}'.format(a, cos(radians(a)))) #Transforma o cos que está em graus em radianos
print(' O ângulo de {:.2f} tem a TANGENTE de {:.2f}'.format(a, tan(radians(a)))) #Transforma o tan que está em graus em radianos