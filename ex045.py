import time
import random
escolhas= ('Tesoura','Papel','Pedra')
print('''[0] ==> TESOURA
[1] ==> PAPEL
[2] ==> PEDRA''')
computador= random.randint(0,2)
jogador= int(input('Escolha uma das alternativas: '))
print('JO-KEN-PÔ')
time.sleep(1.5)
print('O jogador jogou ==> {}'.format(escolhas[jogador]))
print('O computador jogou ==> {}'.format(escolhas[computador]))
if computador==0:
    if jogador==1:
        print('VOCÊ PERDEU!')
    elif jogador==2:
        print('VOCÊ GANHOU!')
    elif computador==jogador:
        print('EMPATE!')
elif computador==1:
    if jogador==0:
        print('VOCÊ GANHOU!')
    elif jogador==2:
        print('VOCÊ PERDEU!')
    elif computador==jogador:
        print('EMPATE!')
elif computador==2:
    if jogador==0:
        print('VOCÊ PERDEU!')
    elif jogador==1:
        print('VOCÊ GANHOU!')
    elif computador==jogador:
        print('EMPATE')
