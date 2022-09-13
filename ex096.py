def linha():
    print('-='*15)
def area(l, c):
    linha()
    a= (l*c)
    print(f'A ÁREA DO LOCAL DE ACORDO COM AS MEDIDAS {l}X{c} É DE ==> {a}m')
    linha()

while True:
    linha()
    l= float(input('INFORME A LARGURA DO LOCAL (m) ==> '))
    c= float(input('INFORME O COMPRIMENTO DO LOCAL (m) ==> '))
    area()
    linha()
    pergunta= str(input('DESEJA CONTINUAR? [S/N]: '))[0].strip().upper()
    linha()
    if (pergunta!='S'and'N'):
        linha()
        print('OPÇÃO INVALIDA TENTE NOVAMENTE DIGITANDO APENAS S OU N')
        pergunta= str(input('DESEJA CONTINUAR? [S/N]: '))[0].strip().upper()
        linha()
    if (pergunta=='S'):
        linha()
        print('RETONANDO...')
        linha()
    if (pergunta=='N'):
        linha()
        print('FINALIZADO')
        linha()
        break