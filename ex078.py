valores= []
maior= []
menor= []
print('-='*15)

for p in range (0,5):
    v= int(input('DIGITE UM VALOR: '))
    valores.append(v)
for p,v in enumerate(valores):
    if (v == (max(valores))):
        maior.append(p)
    if (v == (min(valores))):
        menor.append(p)
print('-='*15)
print(f'VOCÊ DIGITOU OS NÚMEROS {valores}')
print('-='*15)
print(f'O MAIOR NÚMERO DESSA LISTA É {max(valores)} E ESTÁ NA POSIÇÃO {maior}')
print('-='*15)
print(f'O MENOR NÚMERO DESSA LISTA É {min(valores)} E ESTÁ NA POSIÇÃO {menor}')
print('-='*15)