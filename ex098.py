import time

def linha():
    print('-='*15)
def contador(i, f, p):
    linha()
    print(f'CONTAGEM DE {i} ATÉ {f} DE {p} EM {p}')
    if (p<0):
        p= (p*-1)
    if (p==0):
        p=  1
    if i < f:
        c= i
        while c<=f:
            print(f'{c} ', end='', flush=True)
            time.sleep(1)
            c= (c+p)
    else:
        c= i
        while c>=f:
            print(f'{c} ', end='', flush=True)
            time.sleep(1)
            c= (c-p)
    

contador(1, 10, 1)
print()
contador(10, 0, 2)
print()
print('===CONTAGEM PERSONALIZADA===')
inicio= int(input('INFORME O INICIO DA CONTAGEM: '))
fim= int(input('INFORME O FINAL DA CONTAGEM: '))
passo= int(input('INFORME O PASSO DA CONTAGEM: '))
contador(inicio, fim, passo)
print()
linha()