cidade= str(input('Em que cidade você nasceu? ')).strip()
print('A cidade que você nasceu começa com o nome Santo? ==> {} '.format(cidade[:5].upper() == 'SANTO'))