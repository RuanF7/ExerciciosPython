from datetime import datetime
dados = {}
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['Idade'] = datetime.now().year - nasc
dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = (dados['Contratação'] + 35) - nasc
print('=-' * 30)
for k, v in dados.items():
    print(f'   - {k} tem o valor {v}')
