from utilidades.modulosEx109 import moeda

moeda.linha()
n= float(input('DIGITE O PREÇO DO PRODUTO: R$ '))
print(f'A METADE DO PREÇO {moeda.moeda(n)} É ==> {moeda.metade(n, formato=True)}')
print(f'O DOBRO DO PREÇO {moeda.moeda(n)} É ==> {moeda.dobro(n, formato=True)}')
print(f'AUMENTO EM 10% O PREÇO {moeda.moeda(n)} FICA ==> {moeda.aumento(n, formato=True)}')
print(f'REDUZINHO EM 13% O PREÇO {moeda.moeda(n)} FICA ==> {moeda.reduzindo(n, formato=True)}')
moeda.linha()