import time

def linha():
    print('-='*25)
def maior(*num):
    cont = maior = 0
    for n in num:
        print(f'{n} ', end='',flush=True)
        time.sleep(0.5)
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont= (cont+1)
    print()
    print(f'FORAM INFORMADOS ==> {cont} VALORES AO TODO')
    print(f'O MAIOR VALOR INFORMADO FOI DE ==> {maior}')

linha()
maior(2, 9, 4, 5, 7, 1)
linha()
maior(4, 7, 0)
linha()
maior(1, 2)
linha()
maior(6)
linha()
maior()
linha