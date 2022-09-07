n= int(input('Quantos termos você deseja? ==> '))
termo1= 0
termo2= 1
contador= 3
print('{} ==> {} '.format(termo1,termo2), end='')

while contador <= n:
    termo3= (termo1+termo2)
    contador= (contador+1)
    termo1= termo2
    termo2= termo3
    print('==> {} '.format(termo3), end='')
