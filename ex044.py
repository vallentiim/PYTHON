valor= float(input('Informe o valor do produto: '))
print('Escolha a forma de pagamento: ')
print('[1] ==> À vista dinheiro/cheque: 10% de desconto')
print('[2] ==> À vista no cartão: 5% de desconto')
print('[3] ==> Em até 2x no cartão: preço normal')
print('[4] ==> 3x ou mais no cartão: 20% de juros')
print('[5] ==> Sair')
escolha= int(input('==> '))
if escolha == 1:
    desconto= (valor*10)/100
    valordesconto= (valor-desconto)
    print('O valor a ser pago é de ==> R${:.2f}'.format(valordesconto))
elif escolha == 2:
    desconto= (valor*5)/100
    valordesconto= (valor-desconto)
    print('O valor a ser pago é de ==> R${:.2f}'.format(valordesconto))
elif escolha == 3:
    parcelas= (valor/2)
    print('Valor da parcela é de ==> R${:.2f}'.format(parcelas))
elif escolha == 4: 
    valor= valor + ((valor*20)/100)
    parcelas= int(input('Total de parcelas: '))
    valor= (valor/parcelas)
    print('O valor de cada parcela com juros é de ==> R${:.2f}'.format(valor))
elif escolha == 5:
    print('===PROCESSO ENCERRADO===')
else:
    print('OPÇÃO INVALIDA')
print('PAGAMENTO REALIZADO')


    