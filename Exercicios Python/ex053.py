import re
#frase = str(input('Digite uma frase: ')).strip().upper()
##frase = frase.replace(' ', '')# Substitui os espaços
#print(frase.upper())
#frase2 = frase[::-1].upper()#Inverte a string
#print(frase2)
#print('O inverso de {} é {}'.format(frase.upper(), frase2))

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() #Separa numa lista
junto = ''.join(palavras) #Junta tudo da lista
print('Você digitou a frase {}'.format(junto))
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo')