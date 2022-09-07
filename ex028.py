import random
import time
num_ale= random.randint(0, 5)
num= int(input('Qual número entre 0 e 5 a máquina escolheu? '))
print('PROCESSANDO...')
time.sleep(4)
if num == num_ale:
    print('==> Você venceu!')
else:
    print('==> Você perdeu!')
print('A máquina escolheu ==> {} '.format(num_ale))
print('===FIM DO JOGO===')