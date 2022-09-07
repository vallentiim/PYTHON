import math
angulo= float(input('Digite o angulo: '))
seno= math.sin(math.radians(angulo))
cosseno= math.cos(math.radians(angulo))
tangente= math.tan(math.radians(angulo))
print('==> O seno de {}: {:.2f}'.format(angulo, seno))
print('==> O cosseno de {}: {:.2f}'.format(angulo, cosseno))
print('==> A tangente de {}: {:.2f}'.format(angulo, tangente))