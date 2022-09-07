import random

num= random.sample(range(100),5)
lista= (num)
maior = menor = 0
pergunta= 0

while pergunta !='N':
    pergunta= str(input('Deseja continuar?[S/N]: ')).strip().upper()   
    if (pergunta=='S')or(pergunta=='SIM'):
        print('-='*15)
        print(f'LISTA ALEATORIA ==> {lista}')
        print('-='*15)
        print(f'Maior número ==> {max(lista)}')
        print('-='*15)
        print(f'Menor número ==> {min(lista)}')
        print('-='*15)
    if (pergunta=='N')or(pergunta=='NAO')or(pergunta=='NÃO'):
        print('-='*15)
        print('===ENCERRADO===')
        print('-='*15)
        break