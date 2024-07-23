'''from num2words import num2words # Escreve o número por extenso
n = int(input('Digite um número entre 0 e 20: '))
while n > 20 or n < 0:
    print('Tente novamente. Digite um número entre 0 e 20')
    n = int(input('Digite um número entre 0 e 20: '))
num_ptbr = num2words(n, lang='pt-br')
print(f'Você digitou o número {num_ptbr}')'''

# Jeito 2 (Guanabara)
cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'catorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove',
        'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente', end='')
print(f'Você digitou o numero {cont[num]}')