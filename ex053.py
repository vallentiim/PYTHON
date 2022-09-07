frase= str(input('Digite algo: ')).strip().upper()
palavras= frase.split()
frasejunta= ''.join(palavras)
fraseinverso= ''

for letra in range(len(frasejunta)-1,-1,-1):
    fraseinverso = (fraseinverso+frasejunta[letra])
if fraseinverso==frasejunta:
    print('A frase {} é palíndromo.'.format(frase))
else:
    print('A frase {} não é palíndromo.'.format(frase))

    
