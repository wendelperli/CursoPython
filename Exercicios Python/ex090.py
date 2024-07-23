'''n = str(input('Nome: '))
m = float(input('Média: '))
s = ''
print('-=' * 30)
dic = {'nome': n, 'media': m}
print(dic)
print(f'nome é igual a {dic["nome"]}')
print(f'media é igual a {dic["media"]}')
dic['situação'] = 'Aprovado'
if m >= 7:
    dic['situação'] = 'Aprovado'
    print(f'situação é igual a {dic["situação"]}')
if m >= 5 and m < 7:
    dic['situação'] = 'Recuperação'
    print(f'situação é igual a {dic["situação"]}')
if m < 5:
    dic['situação'] = 'Reprovado'
    print(f'situação é igual a {dic["situação"]}')'''

# Guanabara
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')
