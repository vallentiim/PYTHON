num = cont = soma = 0

while True:
    num= int(input('Digite um número ==> '))
    if (num == 999):
        break
    cont= (cont+1)
    soma= (soma+num)

print(f'Você digitou ==> {cont} números, e a soma entre eles é ==> {soma}')