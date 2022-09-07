n1= 0
n2= 0
menu= 0

while menu !=5:
    n1= float(input('Digite o primeiro número ==> '))
    n2= float(input('Digite o segundo número ==> '))
    menu= int(input('''Escolha a operação desejada:
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA
==> '''))
    if (menu != 1) and (menu != 2) and (menu != 3) and (menu != 4) and (menu != 5):
        print('Valor incorreto, Escolha alguma opção.')
    if (menu == 1):
        soma= (n1+n2)
        print('O valor da soma dos números {} e {} é de ==> {}'.format(n1,n2,soma))
    if (menu == 2):
        multi= (n1*n2)
        print('O valor da multiplicação de {} e {} é de ==> {}'.format(n1,n2,multi))
    if (menu == 3):
        if (n1 > n2):
            print('O primeiro número {}, é maior que o segundo {}.'.format(n1,n2))
        elif (n2 > n1):
            print('O segundo número {}, é maior que o primeiro {}.'.format(n2,n1))
        elif (n1 == n2):
            print('Os dois números são iguais.')
    if (menu == 4):
       n1= float(input('Digite outro número ==> '))
       n2= float(input('Digite outro número ==> '))

print('===PROGRAMA ENCERRADO===')