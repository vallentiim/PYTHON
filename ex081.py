numeros= []
print('-='*15)

while True:
    n= int(input('Digite um valor: '))
    numeros.append(n)
    numeros.sort(reverse=True)
    pergunta= str(input('DESEJA CONTINUAR? [S/N]')).strip().upper()
    if (pergunta=='NÃO')or(pergunta=='NAO')or(pergunta=='N'):
        break

print('-='*15)
print(f'A QUANTIDADE DE NÚMEROS DIGITADOS FOI ==> {len(numeros)}')
print('-='*15)
print(f'A ORDEM DOS NÚMEROS ORDENADOS EM ORDEM DECRESCENTE FICA ==> {numeros}')
print('-='*15)
if (5 in numeros):
        print('-='*15)
        print('O NÚMERO 5 ESTÁ ENTRE OS VALORES DIGITADOS.')
        print('-='*15)
else:
    print('-='*15)
    print('O NÚMERO 5 NÃO ESTÁ ENTRE OS VALORES DIGITADOS.') 
    print('-='*15)