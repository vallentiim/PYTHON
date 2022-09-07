casa= float(input('Qual o valor da casa? '))
salario= float(input('Qual o salário do comprador? '))
anos= int(input('Em quantos anos o comprador vai pagar? '))
prestação= casa/ (anos*12)
print('Para pagar uma casa de R${} em {} anos'.format(casa, anos))
print('A prestação será de R${}'.format(prestação))
minimo= (salario*30)/100
if prestação > minimo:
    print('O empréstimo foi negado!')
elif prestação <= (salario*30)/100:
    print('O empréstimo foi concedido!')




