nascimento= int(input('Em que ano você nasceu? '))
ano= 2017
idade= (ano - nascimento)
print('Quem nasceu em {} tem {} anos'.format(nascimento, idade))
if idade < 18:
    falta= (18 - idade)
    print('Você ainda vai se alistar, faltam {} ano(os).'.format(falta))
elif idade == 18:
    print('Está na hora de você se alistar!')
elif idade > 18:
    atraso= (idade - 18)
    print('Caso você não tenha se alistado, você está {} ano(os) atrasado.'.format(atraso))