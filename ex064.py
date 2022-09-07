soma = contador = num = 0

while num != 999:
    num= int(input('Digite um número ==> '))
    if (num!=999):
        soma= (soma+num)
        contador= (contador+1)
    
print('A soma de todos esse números é igual à ==> {} '.format(soma))