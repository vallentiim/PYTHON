pessoas= {}
dados= []
somaIDADE = mediaIDADE = 0

while True:
    print('-='*30)
    pessoas['NOME']= str(input('INFORME O NOME: ')).strip().upper()
    while True:
        pessoas['SEXO']= str(input('INFORME O SEXO [M/F]: ')).strip().upper()
        if (pessoas['SEXO'] in 'MF'):
            break
        else:
            print('ERRO, TENTE NOVAMENTE DIGITANDO APENAS M OU F.')
    pessoas['IDADE']= int(input('INFORME A IDADE: '))
    somaIDADE= (somaIDADE+pessoas['IDADE'])
    dados.append(pessoas.copy())
    mediaIDADE= (somaIDADE/len(dados))
    while True:
        pergunta= str(input('DESEJA CADASTRAR MAIS PESSOAS? [S/N]: ')).strip().upper()
        if (pergunta in 'SN'):
            break
        else:
            print('ERRO, TENTE NOVAMENTE DIGITANDO APENAS S OU N')
    if (pergunta=='N'):
        break

print('-='*30)
print(f'FORAM CADASTRADAS {len(dados)} PESSOAS')
print('-='*30)
print(f'A MÉDIA DE IDADE DAS PESSOAS CADASTRADAS É DE {mediaIDADE:5.2f} ANOS')
print('-='*30)
print('AS MULHERES CADASTRADAS FORAM: ')
for p in dados:
    if (p['SEXO']=='F'):
        print(f'{p["NOME"]}')
print('-='*30)
print(f'AS PESSOAS COM IDADE ACIMA DA MÉDIA SÃO: ',)
for p in dados:
    if(p['IDADE']>mediaIDADE):
        print(f'{p["NOME"]} COM {p["IDADE"]} ANOS')
print('-='*30)