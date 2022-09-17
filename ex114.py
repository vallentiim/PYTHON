import urllib
import urllib.request

try:
    site= urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('NÃO FOI POSSÍVEL CONECTAR AO SITE.')
else:
    print('É POSSÍVEL CONECTAR AO SITE SEM PROBLEMA ALGUM')