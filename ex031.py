km= float(input('Qual a distância da viagem? '))
if km <= 200:
    preço= (0.50*km)
    print('O valor da passagem será de {} R$'.format(preço))
else:
    preço= (0.45*km)
    print('O valor da passagem será de {} R$'.format(preço))
print('===FIM===')