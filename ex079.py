valores= []
print('-='*15)

while True:
    valor= int(input('DIGITE UM VALOR: '))
    if (valor not in valores):
        valores.append(valor)
        valores.sort()
    else:
        print('O VALOR INSERIDO É DUPLICADO.')
    pergunta= str(input('DESEJA CONTINUAR?[S/N]')).strip().upper()
    if (pergunta in 'NNAONÃO'):
        break

print('-='*15)
print(f'Você digitou os valores {valores}')
print('-='*15)