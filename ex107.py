from utilidades.modulosEx107 import moeda

n= float(input('DIGITE O PREÇO DO PRODUTO: R$ '))
print(f'A METADE DO PREÇO R${n} É ==> {moeda.metade(n)}')
print(f'O DOBRO DO PREÇO R${n} É ==> {moeda.dobro(n)}')
print(f'AUMENTO EM 10% O PREÇO R${n} FICA ==> {moeda.aumento(n)}')
print(f'REDUZINHO EM 13% O PREÇO R${n} FICA ==> {moeda.reduzindo(n)}')