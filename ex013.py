salario_normal= float(input('Informe o salário do funcionário: '))
salario_aumento= salario_normal + (salario_normal*15) / 100
print('O funcionário que ganhava {}R$, com o aumento de 15% passou a ganhar {:.2f}R$'.format(salario_normal, salario_aumento))
