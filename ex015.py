dias= int(input('Informe quantos dias o carro foi alugado: '))
km= float(input('Informe quantos km o carro percorreu: '))
valor= (60*dias) + (0.15*km)
print('O total a pagar pelo aluguel do carro é de {}R$'.format(valor))