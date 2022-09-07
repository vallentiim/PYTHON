import random
import time

cont = jogador = 0
escolha= 0
computador= random.randint(0,10)
cores= {'VERDE':'\033[32m',
        'VERMELHO':'\033[31m',
        'LIMPAR':'\033[m'}

while True:
    jogador= int(input('JOGUE UM NÚMERO ==> '))
    escolha= str(input('==> P/I ?')).strip().upper()
    soma= (computador+jogador)
    print('IMPAR, PAR !')
    print(f'COMPUTADOR ==> {computador}')
    time.sleep(1.5)
    if (soma%2==0) and (escolha == 'P'):
        cont= cont+1
        print(f'{cores["VERDE"]}VOCÊ GANHOU!{cores["LIMPAR"]} O RESULTADO FOI PAR!')
        if (soma%2!=0)and(escolha == 'I'):
            cont= cont+1
            print(f'{cores["VERDE"]}VOCÊ GANHOU!{cores["LIMPAR"]} O RESULTADO FOI PAR!')
    else:
        print(f'{cores["VERMELHO"]}VOCÊ PERDEU!{cores["LIMPAR"]}')
        break

print(f'O JOGO ACABOU VOCÊ GANHOU {cont} VEZES')