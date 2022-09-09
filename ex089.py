alunos= []
media= 0

while True:
    print('-='*30)
    nome= str(input('DIGITE O NOME DO ALUNO: '))
    nota1= float(input('DIGITE A PRIMEIRA NOTA: '))
    nota2= float(input('DIGITE A SEGUNDA NOTA: '))
    media= (nota1+nota2)/2
    alunos.append([nome,[nota1,nota2],media])
    pergunta= str(input('DESEJA CONTINUAR? [S/N]: ')).strip().upper()
    if (pergunta=='N'):
        break

print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i,a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')
print('-='*30)
while True:
    print('-='*30)
    opc= int(input('MOSTRAR NOTAS DE QUAL ALUNO? (999 interrompe):'))
    if (opc==999):
        break
    if (opc<=len(alunos)):
        print(f'AS NOTAS DE {alunos[opc][0]} FORAM ==> {alunos[opc][1]}'.upper())