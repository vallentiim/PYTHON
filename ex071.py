valor= int(input('Informe o valor a ser sacado ==> '))
total= valor
cedulas= 50
totalced= 0

while True:
    if total >= cedulas:
        total= (total-cedulas)
        totalced= (totalced+1)
    else:
        if (totalced > 0):
            print(f'TOTAL DE {totalced} CÉDULAS DE R${cedulas}')
        if cedulas==50:
            cedulas=20
        elif cedulas==20:
            cedulas=10
        elif cedulas==10:
            cedulas=1
        totalced= 0
        if total == 0:
            break