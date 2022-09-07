numEX= ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez',
'Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
num= 0

while True:
    num= int(input('Digite um número entre 0 e 20 ==> '))
    if (0>num)or(20<num):
        print('TENTE NOVAMENTE')
    if (0<=num<=20):
        break

print(f'O NÚMERO {num} ESCITO POR EXTENSO É ==> {numEX[num]}')