a1= int(input('Informe o primeiro número da PA ==> '))
razao= int(input('Informe a razão da PA ==> '))
n= int(input('Quantidade de números da PA ==> '))
ultimo= (a1+(n-1)*razao)
ultimo= ultimo+1

for c in range (a1, ultimo, razao):
    print(c)
