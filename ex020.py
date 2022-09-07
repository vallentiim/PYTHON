import math
import random
aluno1= input('Primeiro aluno: ')
aluno2= input('Segundo aluno: ')
aluno3= input('Terceiro aluno: ')
aluno4= input('Quarto aluno: ')
ordem= [aluno1, aluno2, aluno3, aluno4]
random.shuffle(ordem)
print('A ordem de apresentação será ==> {}'.format(ordem))