from datetime import datetime

def linha():
    print('-='*25)
def voto(ano):
    idade= (datetime.now().year-ano)
    if (idade<16):
        print(f'TEM {idade} ANOS ==> VOTO NEGADO')
    if (idade>=16)and(idade<18):
        print(f'TEM {idade} ANOS ==> VOTO OPCIONAL')
    if (idade>=18):
        print(f'TEM {idade} ANOS ==> VOTO OBRIGATÓRIO')

pergunta=0
while True:
    linha()
    anodenasc= int(input('INFORME O ANO DE NASCIMENTO: '))
    voto(anodenasc)
    linha()
    pergunta= str(input('DESEJA CONTINUAR? [S/N]: ')).strip().upper()
    while (pergunta!='N')and(pergunta!='S'):
        pergunta= str(input('OPÇÃO INVALIDA, TENTE NOVAMENTE DIGITANDO APENAS [S ou N]: ')).strip().upper()
    if (pergunta=='N'):
        print('===FINALIZANDO===')
        break