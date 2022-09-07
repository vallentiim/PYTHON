c1= float(input('Informe o comprimento da primeira reta: '))
c2= float(input('Informe o comprimento da segunda reta: '))
c3= float(input('Informe o comprimento da terceira reta: '))
cores= {'Verde':'\033[32m',
        'Limpar':'\033[m'}
if (c1+c2>c3)and(c1+c3>c2)and(c2+c3>c1):
    if (c1==c2==c3):
        print('Essas retas podem formar um triângulo ==> {}equilátero{}.'.format(cores['Verde'],cores['Limpar']))
    elif (c1!=c2!=c3!=c1):
        print('Essas retas podem formar um triângulo == {}escaleno{}'.format(cores['Verde'],cores['Limpar']))
    else:
        print('Essas retas podem formar um triângulo ==> {}isósceles{}'.format(cores['Verde'],cores['Limpar']))
else:
    print('Essas retas não podem formar um triângulo.')