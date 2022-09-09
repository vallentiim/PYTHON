matriz= [[0,0,0],[0,0,0],[0,0,0]]
maior = somaTER = somaP = 0
print('-='*15)

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]= int(input(f'DIGITE UM VALOR PARA [{l},{c}]: '))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
        if (matriz[l][c]%2==0):
            somaP= (somaP+matriz[l][c])
    print()

print('-='*15)
print(f'A SOMA DE TODOS OS VALORES PARES É DE: {somaP}')
print('-='*15)
for l in range(0,3):
    somaTER= (somaTER+matriz[l][2])
print(f'A SOMA DOS VALORES DA TERCEIRA COLUNO É DE: {somaTER}')
print('-='*15)
for c in range(0,3):
    if (c==0):
        maior= matriz[1][c]
    elif (matriz[1][c]>maior):
        maior= matriz[1][c]
print(f'O MAIOR ELEMENTO DA SEGUNDA LINHA É: {maior}') 
print('-='*15)