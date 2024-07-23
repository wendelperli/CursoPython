from datetime import datetime

pessoa = dict()
pessoa['nome'] = str(input('Nome: '))

nasc = int(input('Ano de nascimento: '))
idade = datetime.now().year - nasc

pessoa['idade'] = idade
pessoa['carteira'] = int(input('Carteira de Trabalho (0 não tem)'))
print('-=' * 30)
if pessoa['carteira'] != 0:
    pessoa['contrataçao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contrataçao'] + 35) - datetime.now().year)
    print(pessoa['aposentadoria'])

for k, v in pessoa.items():
    print(f'-  {k} tem o valor {v}.')
