def linha():
    print('-='*20)
def fatorial(num =1):
    """
    ==> CALCULA O FATORIAL DE UM NÚMERO
    num: NÚMERO A SER FATORADO  
    """
    f= 1
    show= str(input('DESEJA MOSTRAR O FATORIAL DESSE NÚMERO?? [S/N]: ')).strip().upper()
    while (show!='N')and(show!='S'):
            show= str(input('OPÇÃO INVALIDA, TENTE NOVAMENTE DIGITANDO APENAS [S ou N]: ')).strip().upper()
    if (show=='N'):
        print('===FINALIZANDO===')
    if (show=='S'):
        for c in range (num, 0, -1):
            print(c,end='')
            if (c>1):
                print(' x ', end='')
            else:
                print(' = ',end='')
            f= (f*c)
        return f

while True:
    n= int(input('INFORME O NÚMERO: '))
    print(fatorial(n))
    pergunta= str(input('DESEJA CONTINUAR? [S/N]: ')).strip().upper()
    while (pergunta!='N')and(pergunta!='S'):
        pergunta= str(input('OPÇÃO INVALIDA, TENTE NOVAMENTE DIGITANDO APENAS [S ou N]: ')).strip().upper()
    if (pergunta=='N'):
        print('===FINALIZANDO===')
        break