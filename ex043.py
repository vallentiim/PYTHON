peso= float(input('Informe o peso: '))
altura= float(input('Informe a altura: '))
imc= (peso/altura**2)
cores= {'Verde':'\033[32m',
        'Limpar':'\033[m'}
if imc<18.5:
    print('==>{}ABAIXO DO PESO{}'.format(cores['Verde'], cores['Limpar']))
elif (imc>=18.5)and(imc<=25):
    print('==>{}PESO IDEAL{}'.format(cores['Verde'], cores['Limpar']))
elif (imc>25)and(imc<=30):
    print('==>{}SOBREPESO{}'.format(cores['Verde'], cores['Limpar']))
elif (imc>30)and(imc<=40):
    print('==>{}OBESIDADE{}'.format(cores['Verde'], cores['Limpar']))
elif imc>40:
    print('==>{}OBESIDADE MÓRBIDA{}'.format(cores['Verde'], cores['Limpar']))