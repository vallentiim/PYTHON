times= ('','Palmeiras','Flamengo','Corinthians','Sport','Internacional','Fluminese','AtleticoMG','America','Santos','Chapecoense','Bragantino',
'Goiás','Fortaleza','Botafogo','São Paulo','Ceará','Cuiabá','Coritiba','Avaí','Nautico')
posiçaoCHAPECO= times.index('Chapecoense')
escolha= 0

while escolha!='N':
    escolha= str(input('Deseja saber informações sobre a tabela do campeonato?[S/N]: ')).strip().upper()
    if (escolha=='S')or(escolha=='SIM'):
        print('-='*45)
        print(f'==>Os cinco primeiros colocados da tabela são ==> {times[1:5+1]}')
        print('-='*45)
        print(f'==>Os quatro últimos colocados da tabela são ==> {times[17:20+1]}')
        print('-='*45)
        print(f'==>Os times em ordem alfabetica ==> {sorted(times)}')
        print('-='*45)
        print(f'==>O time chapecoense está na {posiçaoCHAPECO}º posição')
        print('-='*45)
    elif (escolha=='N')or(escolha=='NÃO')or(escolha=='NAO'):
        print('-='*45)
        print('===ENCERRADO===')
        print('-='*45)
        break