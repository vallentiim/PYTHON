sexo= 'M' and 'F'
quantM= 0
quantF= 0

while sexo != 'SAIR':
    sexo= str(input('\nM ==> MASCULINO\nF ==> FEMININO \nDigite [5] PARA SAIR DA PESQUISA\nInforme seu sexo [M/F]:')).strip().upper()[0]
    if (sexo =='M' or sexo == 'F'):
        print('Sexo registrado.')
    if (sexo !='M') and (sexo != 'F') and (sexo != 'SAIR'):
        print('Valor incorreto, digite novamente: ')
    if (sexo == 'M'):
        quantM= (quantM + 1)
    if (sexo == 'F'):
        quantF= (quantF +1)
print('Ao total, houve:\n==>{} HOMENS\n==>{} MULHERES'.format(quantM, quantF))