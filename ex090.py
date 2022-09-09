aluno= {}
print('-='*30)
print('                 BOLETIM ESCOLAR                 ')
print('-='*30)

while True:
    aluno['nome']= str(input('DIGITE O NOME DO ALUNO: ')).strip().upper()
    aluno['media']= float(input(f'DIGITE A MÉDIA DE {aluno["nome"]} '))
    if (aluno['media']>=7):
        print('-='*30)
        print(f'O ALUNO(A) {aluno["nome"]} ESTÁ COM MÉDIA {aluno["media"]} ==> APROVADO')
        print('-='*30)
    else:
        print('-='*30)
        print(f'O ALUNO(A) {aluno["nome"]} ESTÁ COM MÉDIA {aluno["media"]} ==> REPROVADO')
        print('-='*30)
    aluno.clear()
    pergunta= str(input('DESEJA CONTINUAR? [S/N]: ')).strip().upper()
    if (pergunta=='N'):
        print('-='*30)
        print('                 FINALIZADO                 ')
        break
print('-='*30)
