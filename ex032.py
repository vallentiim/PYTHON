import calendar
ano= int(input('Informe o ano: '))
if calendar.isleap(ano):
    print('O ano é ==> Bissexto')
else:
    print('O ano não é bissexto')