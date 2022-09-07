import random
import time

jogador= '?'
computador= random.randint(0, 10)
quantERRO= 1
cores= {'VERDE':'\033[32m',
        'VERMELHO':'\033[31m',
        'LIMPAR':'\033[m'}

while jogador!=computador:
    jogador= int(input('PENSEI EM UM NÚMERO DE 0 A 10, TENTE ADIVINHAR!\n==> '))
    print('PROCESSANDO...')
    time.sleep(2)
    if (jogador!=computador):
        print('==> {}ERROU!{}'.format(cores['VERMELHO'], cores['LIMPAR']))
    if (jogador!=computador):
         quantERRO= (quantERRO+1)
    if (jogador == computador):
        print('==> {}ACERTOU!{}'.format(cores['VERDE'], cores['LIMPAR']))

print('VOCÊ ACERTOU DEPOIS DE ==> {} TENTATIVAS'.format(quantERRO))