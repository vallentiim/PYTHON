print('-='*15)
valores= (int(input('Digite o primeiro valor ==> ')),
int(input('Digite o segundo valor ==> ')),
int(input('Digite o terceiro valor ==> ')),
int(input('Digite o quarto e ultimo valor ==> ')))
print('-='*15)

print(f'VOCÊ DIGITOU OS VALORES {valores}')
print('-='*15)
print(f'O NÚMERO 9 APARECEU {valores.count(9)} VEZES')
print('-='*15)
print(f'O NÚMERO 3 APARECEU NA POSIÇÃO {valores.index(3, 1)+1}')
print('-='*15)
print(f'OS NÚMEROS PARES SÃO ==> ',end='')
for n in valores:
    if n%2==0:
        print(n,end=' ')