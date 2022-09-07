somaidade= 0
maioridadehomem= 0
nomevelho= ''
mulheridade20= 0

for pessoa in range(1, 4+1):
    print('{} PESSOA'.format(pessoa))
    nome= str(input('NOME ==> ')).strip().upper()
    idade= int(input('IDADE ==> '))
    sexo= str(input('SEXO ==> [M/F]')).strip().upper()
    somaidade= (somaidade+idade)
    mediaidade= (somaidade/4)
    if pessoa == 1 and sexo in 'M':
        maioridadehomem= idade
        nomevelho= nome
    if sexo in 'M' and idade > maioridadehomem:
        maioridadehomem= idade
        nomevelho= nome
    if sexo in 'F' and idade < 20:
        mulheridade20= (mulheridade20 +1)
        
print('\nA média de idade do grupo é ==> {}.'.format(mediaidade))
print('\nO homem mais velho se chama ==> {} e tem {} anos'.format(nomevelho, maioridadehomem))
print('\nEntre as 4 pessoas, {} são mulheres com menos de 20 anos.'.format(mulheridade20))

    
