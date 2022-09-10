time= []
jogador= {}
partidas= []

while True:
    print('-='*30)
    jogador.clear()
    jogador['NOME']= str(input('NOME DO JOGADOR: ')).upper()
    tot= int(input(f'QUANTAS PARTIDAS {jogador["NOME"]} JOGOU?: '))
    partidas.clear()
    for c in range (0,tot):
        partidas.append(int(input(f' QUANTOS GOLS {jogador["NOME"]} NA PARTIDA {c+1}?')))
    jogador['GOLS']= (partidas[:])
    jogador['TOTAL']= (sum(partidas))
    time.append(jogador.copy())
    while True:
        pergunta= str(input('DESEJA CADASTRAR OUTRO JOGADOR? [S/N]: ')).strip().upper()
        if (pergunta=='S'or'N'):
            break
        else:
            print('VALOR INCORRETO, DIGITE APENAS S OU N')
    if (pergunta=='N'):
        break
print('-='*30)
print('COD',end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
for k,v in enumerate(time):
    print(f'{k:>3}',end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-='*30)
while True:
    busca= int(input('MOSTRAR DADOS DE QUAL JOGADOR? (999 para o codigo.): '))
    if (busca==999):
        break
    if (busca>=len(time)):
        print(f'NÃO EXISTE JOGADOR COM O CÓDIGO {busca}')
    else:
        (f'==> LEVANTAMENTO DO JOGADOR {time[busca] ["NOME"]}: ')
        for i, g in enumerate(time[busca]['GOLS']):
            print(f'   NO JOGO {i+1} FEZ {g} GOLS')