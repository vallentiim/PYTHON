jogador= {}
partidas= []
quantPART = quantGOLS = cont = 0
print('-='*30)
print('                 INFORMAÇÕES DO JOGADOR                 ')
print('-='*30)

while True:
    jogador['nome']= str(input('INFORME O NOME DO JOGADOR: ')).upper()
    jogador['Quantidade de partidas']= int(input(f'QUANTAS PARTIDAS {jogador["nome"]} JOGOU?: '))
    quantPART= jogador['Quantidade de partidas']
    resp= str(input('DIGITE X PARA PROSSEGUIR: ')).strip().upper()
    if (resp=='X'):
        break
print('-='*30)

for c in range(0, quantPART):
    partidas.append(int(input(f'QUANTOS GOLS {jogador["nome"]} FEZ NA {c+1} PARTIDA ')))
jogador['gols']= (partidas[:])
quantGOLS= (sum(partidas))
print('-='*30)
print(f'O JOGADOR {jogador["nome"]} JOGOU {quantPART} PARTIDAS')

for p, g in enumerate(partidas):
    print('-='*30)
    print(f'==> NA {p+1} PARTIDA, FEZ {g} GOLS')
print('-='*30)
print(f'==> AO TODO FEZ, {quantGOLS} GOLS')
print('-='*30)