nascimento= int(input('Qual ano você nasceu? '))
ano= 2017
idade= (ano - nascimento)
cores= {'Verde':'\033[32m',
        'Limpar':'\033[m'}
print('Você tem ==> {} anos'.format(idade))
if idade <= 9:
    print('Você está na categoria ==> {}MIRIM{}'.format(cores['Verde'], cores['Limpar']))
elif idade <=14 and idade > 9:
    print('Você está na categoria ==> {}INFANTIL{}'.format(cores['Verde'], cores['Limpar']))
elif idade <=19 and idade > 14:
    print('Você está na categoria ==> {}JUNIOR{}'.format(cores['Verde'], cores['Limpar']))
elif idade == 20:
    print('Você está na categoria ==> {}SÊNIOR{}'.format(cores['Verde'], cores['Limpar']))
elif idade > 20:
    print('Você está na categoria ==> {}MASTER{}'.format(cores['Verde'], cores['Limpar']))