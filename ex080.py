valores= []

for p in range(0,5):
    v= int(input('Digite um valor: '))
    if (p==0)or(v>valores[-1]):
        valores.append(v)
    else:
        pos= 0
        while pos<len(valores):
                if v<=valores[pos]:
                    valores.insert(pos, v)
                    break
                pos= (pos+1)

print('-='*15)
print(f'Os valores digitados foram ==> {valores}')
print('-='*15)