print('-='*15)
exp= str(input('DIGITE A EXPRESSÃO: '))
print('-='*15)

lista= []

for s in exp:
    if (s=='('):
        lista.append('(')
    elif (s==')'):
        if (len(lista)>0):
            lista.pop()
        else:
            lista.append(')')
            break

if (len(lista)==0):
    print('SUA EXPRESSÃO ESTÁ VÁLIDA!')
    print('-='*15)
else:
    print('SUA EXPRESSÃO NÃO É VÁLIDA!')
    print('-='*15)