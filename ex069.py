sexo = idade = pergunta = quantF = quantM = idadeF = idadeCONT = 0

while True:
    idade= int(input('Informe a idade ==> '))
    sexo= str(input('Informe o sexo [M/F]==> ')).strip().upper()
    pergunta= str(input('Você deseja continuar? Caso não queira digite a letra [S/N] ')).strip().upper()
    if (sexo == 'M'):
        quantM= (quantM+1)
    if (idade > 18):
        idadeCONT= (idadeCONT+1)
    if (idade < 20)and(sexo == 'F'):
        idadeF= (idadeF+1)
    if (pergunta == 'N'):
        break

print(f'AO TOTAL ==> {idadeCONT} PESSOAS TEM MAIS DE 18 ANOS')
print(f'AO TOTAL ==> {quantM} HOMENS FORAM CADASTRADOS')
print(f'AO TOTAL ==> {idadeF} MULHERES TEM MENOS DE 20 ANOS')