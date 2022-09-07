num= int(input('Informe um número: '))
print('Escolha a opção para converter o número: ')
escolha= int(input('Escolha uma alternativa para converter o número: \n[1]  ==> binário\n[2]  ==> octal\n[3]  ==> hexadecimal\n[4] ==> sair\n==>'))
if escolha == 1:
    bin= (bin(num))
    print('O número na forma binária é: {}'.format(bin))
elif escolha == 2:
    oct= (oct(num))
    print('O número na format octal é: {}'.format(oct))
elif escolha == 3:
    hex= (hex(num))
    print('O número na forma hexadecimal é: {}'.format(hex))
elif escolha == 4:
    print('O programa foi encerrado!')
else:
    print('Opção invalida!')

