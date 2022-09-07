a= 3
b= 4
cores= {'Azul':'\033[34m' , 
        'Amarelo':'\033[33m' , 
        'Vermelho':'\033[31m' ,
        'Verde':'\033[32m', 
        'Limpar':'\033[m'}
print('Os valores de a e b são respectivamente: {}{}{} e {}{}{}'.format(cores['Azul'], a , cores['Limpar'] , cores['Vermelho'] , b , cores['Limpar']))