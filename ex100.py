import random

num= []
numPAR= []

def linha():
    print('-='*20)
def sorteia():
    for n in range(5):
        num.append(random.randint(1, 50))
    print(f'LISTA DE 5 NÚMEROS {num}')
def somaPAR():
    soma= 0
    for n in num:
        if (n%2==0):
            numPAR.append(n)
            soma= sum(numPAR)
    print(f'SOMANDO OS NÚMEROS PARES {numPAR} O RESULTADO É IGUAL À ==> {soma} ')

linha()
sorteia()
somaPAR()
linha()