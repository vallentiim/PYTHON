produto = preço = pergunta = totalG = preço1000 = prodBARATO = nomeBARATO = cont = 0

while True:
    produto= str(input('Informe o nome do produto ==> '))
    preço= float(input('Informe o preço do produto ==> '))
    cont= (cont+1)
    pergunta= str(input('Quer continuar? [S/N]')).strip().upper()
    if (preço >= 0):
        totalG= (totalG+preço)
    if (preço > 1000):
        preço1000= (preço1000+1)
    if (cont== 1):
        prodBARATO= preço
    else:
        if preço < prodBARATO:
            prodBARATO= preço
            nomeBARATO= produto         
    if (pergunta == 'N'):
        break

print(f'O TOTAL GASTO NA COMPRA FOI DE ==> {totalG}')
print(f'NO TOTAL ==> {preço1000} PRODUTOS CUSTAM MAIS DE R$1000')
print(f'O NOME DO PRODUTO MAIS BARATO É ==> {nomeBARATO} E ELE CUSTA ==> {prodBARATO}')
