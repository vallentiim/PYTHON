from utilidades.modulosEx112 import moeda
from utilidades.modulosEx112 import dados

while True:
    moeda.linha()
    n= dados.LeiaDinheiro(('INFORME O VALOR DO PRODUTO: '))
    moeda.resumo(n, 80, 35)
    moeda.linha()
    pergunta= str(input('DESEJA CONTINUAR? [S/N]: ')).strip().upper()
    while (pergunta!='N')and(pergunta!='S'):
        pergunta= str(input('OPÇÃO INVALIDA, TENTE NOVAMENTE DIGITANDO APENAS [S ou N]: ')).strip().upper()
    if (pergunta=='N'):
        print('===FINALIZANDO===')
        moeda.linha()
        break