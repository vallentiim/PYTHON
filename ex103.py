def linha():
    print('-='*20)
def ficha(nome='DESCONHECIDO', gols=0):
    print(f'NOME DO JOGADOR ==> {nome}')
    print(f'QUANTIDADE DE GOLS NO CAMPEONATO ==> {gols} GOL(S)')

while True:
    linha()
    n= str(input('NOME DO JOGADOR: '))
    g= str(input('QUANTIDADE DE GOLS NO CAMPEONATO: '))
    if g.isnumeric():
        g= int(g)
    else:
        g= 0
    if n.strip()=='':
        ficha(gols=0)
    else:
        ficha(n,g)
    linha()
    pergunta= str(input('DESEJA CONTINUAR? [S/N]')).strip().upper
    while (pergunta!='N')and(pergunta!='S'):
        pergunta= str(input('OPÇÃO INVALIDA, TENTE NOVAMENTE DIGITANDO APENAS [S ou N]: ')).strip().upper()
    if (pergunta=='N'):
        print('===FINALIZANDO===')
        break