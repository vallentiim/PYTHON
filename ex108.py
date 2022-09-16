from utilidades.modulosEx108 import moeda

moeda.linha()
n= float(input('DIGITE O PREÇO DO PRODUTO: R$ '))
print(f'A METADE DO PREÇO {moeda.moeda(n)} É ==> {moeda.moeda(moeda.metade(n))}')
print(f'O DOBRO DO PREÇO {moeda.moeda(n)} É ==> {moeda.moeda(moeda.dobro(n))}')
print(f'AUMENTO EM 10% O PREÇO {moeda.moeda(n)} FICA ==> {moeda.moeda(moeda.aumento(n))}')
print(f'REDUZINHO EM 13% O PREÇO {moeda.moeda(n)} FICA ==> {moeda.moeda(moeda.reduzindo(n))}')
moeda.linha()