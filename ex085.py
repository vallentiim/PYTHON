lista= [[], []]
valor= 0
print('-='*15)

for c in range(0,7):
    valor= int(input('DIGITE UM NÚMERO: '))
    if (valor%2==0):
        lista[0].append(valor)
        lista[0].sort()
    elif(valor%2!=0):
        lista[1].append(valor)
        lista[1].sort()

print('-='*15)
print(f'VALORES PARES DA LISTA ==> {lista[0]}')
print('-='*15)
print(f'VALORES ÍMPARES DA LISTA ==> {lista[1]}')
print('-='*15)