nota1= float(input('Informe a primeira nota: '))
nota2= float(input('Informe a segunda nota: '))
media= (nota1 + nota2)/2
cores= {'Verde':'\033[32m',
        'Vermelho':'\033[31m',
        'Amarelo':'\033[33m',
        'Limpar':'\033[m'}
print('Sua média é: {}'.format(media))
if media < 5:
    print('==>{}REPROVADO!{}'.format(cores['Vermelho'],cores['Limpar']))
elif media >= 5 and media <=6.9:
    print('{}RECUPERAÇÃO!{}'.format(cores['Amarelo'],cores['Limpar']))
elif media >= 7:
    print('{}APROVADO!{}'.format(cores['Verde'],cores['Limpar']))