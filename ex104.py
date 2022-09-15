def linha():
    print('-='*20)
def leiaint(num):
    ok= False
    valor= 0
    while True:
        n= str(input(num))
        if (n.isnumeric):
            valor= int(n)
            ok= True
        else:
            n= int(input('OPÇÃO INVALIDA, TENTE NOVAMENTE DIGITANDO APENAS NÚMEROS: '))
        if ok:
            break
    print(f'VOCÊ INFORMOU O VALOR ==> {valor}')


while True:
    linha()
    n= leiaint('DIGITE UM NÚMERO: ')
    linha()
    pergunta= str(input('DESEJA CONTINUAR? [S/N]: ')).strip().upper()
    while (pergunta!='N')and(pergunta!='S'):
        pergunta= str(input('OPÇÃO INVALIDA, TENTE NOVAMENTE DIGITANDO APENAS [S ou N]: ')).strip().upper()
    if (pergunta=='N'):
        print('===FINALIZANDO===')
        break
linha()