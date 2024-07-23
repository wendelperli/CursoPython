from math import floor  #Arredonda um número pra baixo, 'math.ceil()' arredonda pra cima, round() para o mais próximo
v = float(input('Qual é a velocidade atual do carro? '))
if v <= 80:
    print('Continue assim. Boa Viagem')
else:
    v = floor(v)
    ve = (v - 80)
    m = ve * 7
    print('Você foi multado! Você Excedeu o limite permitido que é de 80Km/h')
    print('A multa vai custar R${:.2f} '.format(m))
