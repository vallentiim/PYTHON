n1= int(input('Digite o primeiro número: '))
n2= int(input('Digite o segundor número: '))
cores= {'Azul':'\033[34m',
        'Limpar':'\033[m'}
if n1 > n2:
    print('O primeiro número ==> {}{}{} é MAIOR que o segundo número ==> {}{}{}.'.format(cores['Azul'],n1,cores['Limpar'],cores['Azul'],n2,cores['Limpar']))
elif n2 > n1:
    print('O segundo número ==> {}{}{} é MAIOR que o primeiro número ==> {}{}{}.'.format(cores['Azul'],n2,cores['Limpar'],cores['Azul'],n1,cores['Limpar']))
elif n1 == n2:
    print('Os dois números são iguais.')
print('===FIM DO PROCESSO===')
