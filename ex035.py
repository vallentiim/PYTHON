reta1= float(input('Informe o comprimento da primeira reta: '))
reta2= float(input('Informe o comprimento da segunda reta: '))
reta3= float(input('Informe o comprimento da terceira reta: '))
if (reta1+reta2>reta3)and(reta1+reta3>reta2)and(reta2+reta3>reta1):
    print('É possível fazer um triângulo com essas retas.')
else:
    print('Não é possível fazer um triângulo com essas retas.')