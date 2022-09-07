num= int(input('Informe um número ==> '))
total= 0
cores= {'Vermelho':'\033[31m',
        'Limpar':'\033[m'}
print('O número ==> {} é divisível por: '.format(num))

for c in range(1, num+1):
    if (num % c == 0):
        print('{}'.format(cores['Vermelho']), end='')
        total= (total+1)
    else:
        print('{}'.format(cores['Limpar']), end='')
    print('{} '.format(c), end='')
print('{} O número {}, foi divisível {} vezes.'.format(cores['Limpar'], num, total))


if total == 2:
    print('O número {} é ==> PRIMO'.format(num))
else:
    print('O número {} não é primo.'.format(num))