import math

num= int(input('Informe um número ==> '))
contador= num

while contador > 0:
    print(' {}'.format(contador), end='')
    if (contador > 1):
        print(' x' , end='')
    else:
        print( ' = {}'.format(math.factorial(num)))
    contador= (contador-1)
