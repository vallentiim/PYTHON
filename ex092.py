import datetime

dados= {}

while True:
    print('-='*30)
    dados['Nome']= str(input('INFORME O NOME: '))
    nasc= int(input('INFORME O ANO DE NASCIMENTO: '))
    dados['Idade']= (datetime.datetime.now().year-nasc)
    dados['ctps']= int(input('INFORME A CARTEIRA DE TRABALHO (DIGITE 0 SE NÃO POSSUIR): ')) 
    if (dados['ctps']==0):
        for k, v in dados.items():
            print(f'{k} ==> {v}') 
        break
    dados['Ano de contratação']= int(input('INFORME O ANO DE CONTRATAÇÃO: '))
    dados['Salario']= float(input('INFORME O SALÁRIO: R$ '))
    dados['Aposentadoria']= dados['Idade']+((dados['Ano de contratação']+35)-datetime.datetime.now().year)
    print('-='*30)

for k, v in dados.items():
    print(f'{k} ==> {v}')
    print('-='*30)