largura= float(input('Informe a largura da parede: '))
altura= float(input('Informe o comprimento da parede: '))
area= (altura*largura)
quant_tinta= (altura*largura)/2
print('A parede tem uma dimensão de {}x{}, e tem uma área de {} m.'.format(largura, altura, area))
print('Será necessário {} litros de tinta para pintar a parede.'.format(quant_tinta))