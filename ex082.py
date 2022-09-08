lista= []
listaP= []
listaI= []
print('-='*15)

while True:
    n= int(input('DIGITE UM VALOR: '))
    lista.append(n)
    lista.sort()
    pergunta= str(input('DESEJA CONTINUAR? [S/N]: ')).strip().upper()
    if (pergunta=='NÃO')or(pergunta=='NAO')or(pergunta=='N'):
        break  
print('-='*15)
for n in lista:
    if (n%2==0):
        listaP.append(n)
        listaP.sort()
    else:
        listaI.append(n)
        listaI.sort()

print(f'A LISTA DE NÚMEROS DIGITADOS ==> {lista}')
print('-='*15)
print(f'A LISTA DE NÚMEROS PARES ==> {listaP}')
print('-='*15)
print(f'A LISTA DE NÚMEROS ÍMPARES ==> {listaI}')
print('-='*15)