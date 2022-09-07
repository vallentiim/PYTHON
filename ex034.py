salario= int(input('Informe o salário: '))
if salario > 1.250:
    aumento= (salario*10)/100
    salario= (salario + aumento)
    print('Você recebeu um aumento de 10%!')
    print('Seu salário ficou ==> {}'.format(salario))
else:
    aumento= (salario * 15) / 100
    salario= (salario + aumento)
    print('Você recebeu um aumento de 15%!')
    print('Seu salário ficou ==> {}'.format(salario))