preço_normal= float(input('Informe o preço do produto: '))
preço_desconto= preço_normal - (preço_normal * 5) / 100
print('O produto que custava {}R$, com o desconto de 5% passou a custar {}R$'.format(preço_normal, preço_desconto))