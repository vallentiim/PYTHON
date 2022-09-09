dados= []
lista= []
maior = menor = 0
print('-='*15)

while True:
    dados.append(str(input('DIGTE O NOME: ')))
    dados.append(float(input('DIGITE O PESO: ')))
    if len(lista) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    lista.append(dados[:])
    dados.clear()
    pergunta= str(input('DE SEJA CONTINUAR? [S/N]: ')).strip().upper()
    print('-='*15)
    if (pergunta in 'Nn'):
        break

print(f'O TOTAL DE PESSOAS CADASTRADAS FOI DE {len(lista)}')
print('-='*15)
print(f'AS PESSOAS MAIS PESADAS DA LISTA SÃO {maior}. Peso de ==> ',end='')
for p in lista:
    if (p[1]==maior):
        print(f'{p[0]}',end='')
print(f'\nAS PESSOAS MAIS LEVES DA LISTA SÃO {menor}. Peso de ==> ',end='')
for p in lista:
    if (p[1]==menor):
        print(f'{p[0]}',end='')


