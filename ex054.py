import datetime
maior=0
menor=0

for pessoas in range(1, 7+1):
    anonasci= int(input('Informe o {} ano de nascimento: '.format(pessoas)))
    anoatual= datetime.date.today().year
    idade= (anoatual-anonasci)
    if idade>=21:
      maior= (maior+1)
    elif idade<21:
        menor= (menor+1)
        
print('Entre as 7 pessoas: \n==>{} são de maioridade \n==>{} são de menoridade'.format(maior, menor))
