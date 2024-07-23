lista = []
aluno = []
mostrar = 0
num = 0
while True:
    num = num
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    aluno.append(num)
    aluno.append(nome)
    aluno.append(n1)
    aluno.append(n2)
    aluno.append(media)
    lista.append(aluno[:])
    aluno.clear()
    resp = str(input('Quer continuar? [S / N]')).upper()
    num = num + 1
    if resp in 'N':
        break
print('-=' * 30)
print(f'{"No.":<4} {"Aluno":<10} {"Média":>8}')
for c in range(0, len(lista)):
    print(f'{lista[c][0]:<4}', f'{lista[c][1]:<10}', f'{lista[c][4]:>8}')

while True:
    mostrar = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))
    for c in range(0, len(lista)):
        if mostrar == lista[c][0]:
            print(f'Notas de {lista[c][1]} são {lista[c][2]} e {lista[c][3]}')
    if mostrar == 999:
        break
