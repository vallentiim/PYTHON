def linha():
    print('-='*20)
def leiaINT(num):
    while True:
        try:
            n= int(input(num))
        except (ValueError, TypeError):
            print('TIVEMOS PROBELMAS COM OS VALORES DIGITADOS! TENTE NOVAMENTE')
            continue
        except (KeyboardInterrupt):
            print('O USUÁRIO PREFERIU NÃO INFORMAR O NÚMERO!')
            continue
        else:
            return n
def leiaFLOAT(num):
    while True:
        try:
            n= float(input(num))
        except (ValueError, TypeError):
            print('TIVEMOS UM PROBLEMA COM OS VALORES DIGITADOS! TENTE NOVAMENTE')
            continue
        except (KeyboardInterrupt):
            print('O USUÁRIO NÃO INFORMOU UM NÚMERO!')
            continue
        else:
            return n

linha()
nint= leiaINT('INFORME UM NÚMERO INTEIRO: ')
linha()
nfloat= leiaFLOAT('INFORME UM NÚMERO FLUTUANTE: ')
linha()
print(f'O VALOR INTEIRO DIGITADO FOI ==> {nint}\nO VALOR EM FLOAT DIGITADO FOI ==> {nfloat}')
linha()