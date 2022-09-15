c= ('\033[m', #0-sem cor
    '\033[0;30.41m', #1-vermelho
    );

def ajuda(com):
    help(com)
def titulo(txt, cor=0):
    tam= len(txt)+4
    print(c[cor], end='')
    print('-='*tam)
    print(f'   {txt}')
    print('-='*tam)
    print(c[0], end='')

comando= ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 1)
    comando= str(input('FUNÇÃO OU BIBLIOTECA >'))
    if (comando.upper()=='FIM'):
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)