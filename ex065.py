contador = media = soma = maior = menor= 0
pergunta='S'

while pergunta != 'N':
    num= float(input('Digite um número ==> '))
    soma= (soma+num)
    contador= (contador+1) 
    pergunta= str(input('DESEJA CONTINUAR? [S/N] ==> ')).strip().upper()
    media= (soma/contador)
    if contador == 1:
        maior= num
        menor= num
    else:
        if num > maior:
            maior = num
        if num < menor:
            maior = num

print('A média da soma de todos os números foi de ==> {}'.format(media))
print('''O maior número ==> {}  
O menor número ==> {}'''.format(maior, menor))