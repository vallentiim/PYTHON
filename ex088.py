import random

jogos= []
sorteio= []
quantJOGOS= int(input('QUANTOS JOGOS VOCÊ QUER SORTEAR? '))
total= 1

while total<=quantJOGOS:
    cont= 0
    while True:
        n= random.randint(1, 60)
        if (n not in sorteio):
            sorteio.append(n)
            cont= (cont+1)
        if (cont>=6):
            break

    sorteio.sort()
    jogos.append(sorteio[:])
    sorteio.clear()
    total= (total+1)

for i, l in enumerate(jogos):
    print('-='*15)
    print(f'JOGO {i+1}: {l}')
    
print('-='*15)