soma= 0
contador= 0
for c in range(0, 500+1):
    if c%2!=0:
        if c%3==0:
            contador= (contador+1)
            soma= (soma+c)
print('A soma dos números ímpares e multiplos de 3 entre 1 e 500 é: {}'.format(soma))