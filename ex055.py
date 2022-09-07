maior= 0
menor= 0

for pessoa in range(1, 5+1):
    peso= float(input('Informe o {} peso: '.format(pessoa)))
    if pessoa == 1:
        maior= peso
        menor= peso
    else:
        if peso > maior:
            maior= peso
        if peso < menor:
            menor= peso
                
print('Entre as 5 pessoas é possível informar: \n==> {} maior peso \n==> {} menor peso'.format(maior, menor))
