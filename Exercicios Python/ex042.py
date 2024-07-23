v1 = float(input('Primeiro segmento: '))
v2 = float(input('Segundo segmento: '))
v3 = float(input('Terceiro segmento: '))

if (v1 < v2 + v3) and (v2 < v1 + v3) and (v3 < v1 + v2):

    if v1 == v2 and v2 == v3:
        print('Os segmentos acima podem formar um triângulo EQUILATERO!')

    elif (v1 == v2 and v2 != v3) or (v2 == v3 and v3 != v1) or (v1 == v3 and v1 != v2):
        print('Os segmentos acima podem formar um triângulo ISÓCELES!')

    elif (v1 != v2) and (v1 != v3) and (v2 != v3):
        print('Os segmentos acima podem formar um triângulo ESCALENO!')

else:
    print('Os segmentos acima NÃO PDEM FORMAR um triângulo!')