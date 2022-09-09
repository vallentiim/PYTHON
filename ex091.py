import random
import time
import operator

jogo= {'jogador1':random.randint(1,6),
        'jogador2':random.randint(1,6),
        'jogador3':random.randint(1,6),
        'jogador4':random.randint(1,6)}
rank= []
maior= 0
print('VALORES SORTEADOS: ')

for k, v in jogo.items():
    print('-='*30)
    print(f'{k} tirou ==> {v} no dado.')
    time.sleep(1)
rank= sorted(jogo.items(), key=operator.itemgetter(1), reverse=True)
print('-='*30)
print('   ==RANKING==')
for i, v in enumerate(rank):
    print(   f'{i+1} LUGAR: {v[0]} COM {v[1]}')
    time.sleep(1)
    
    
 