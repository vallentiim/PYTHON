km= float(input('Qual a velocidade do carro? '))
if km > 80:
    multa= (km - 80) * 7
    print('Você recebeu uma multa de ==> {}R$'.format(multa))
else:
    print('Você não foi multado!')