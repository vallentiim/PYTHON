import math
cateto_op= float(input('Digite o comprimento do cateto oposto: '))
cateto_ad= float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa= math.sqrt ((math.pow(cateto_op, 2)) + (math.pow(cateto_ad, 2)))
print('==> De acordo com o valor dos catetos, a hipotenusa mede: {:.2f} cm'.format(hipotenusa))
