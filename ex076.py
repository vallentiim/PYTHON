lista= ('LÁPIS',1.75,  
        'BORRACHA',2,
        'CADERNO',15.90,
        'ESTOJO',25,
        'COMPASSO',10)

print('-='*20)
print(' '*10,'LISTAGEM DE PREÇOS')
print('-='*20)
for pos in range(0, len(lista)):
    if (pos%2==0):
        print(f'{lista[pos]:.<30}',end='')
    else:
        print(f'R${lista[pos]}')
print('-='*20)

