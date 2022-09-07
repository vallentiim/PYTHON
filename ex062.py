a1= int(input('Digite o primeiro termo da PA ==> '))
razao= int(input('Digite a razão da PA ==> '))
termo= a1
contador= 1
n= int(input('Número de termos da PA ==> '))

while contador <= n:
    print('{} ==> '.format(termo), end='')
    termo= (termo+razao)
    contador= (contador+1)