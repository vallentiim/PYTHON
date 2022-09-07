a1= int(input('Digite o primeiro termo da PA ==> '))
razao= int(input('Digite a razão da PA ==> '))
termo= a1
contador= 1

while contador <= 10:
    print('{} ==> '.format(termo), end='')
    termo= (termo+razao)
    contador= (contador+1)