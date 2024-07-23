peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)

print('O IMC dessa pessoa é {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está ABAIXO DO PESO normal!')
elif imc >= 18.5 and imc < 25:
    print('Você está no PESO IDEAL!')
    print('PARABENS, você está na faixa de PESO NORMAL!')
elif imc >= 25 and imc < 30:
    print('Você está com SOBREPESO!')
elif imc >= 30 and imc < 40:
    print('Você está em OBESIDADE!')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')


