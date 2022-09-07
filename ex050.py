soma= 0
contador= 0

for c in range(1, 6+1):
    num= int(input('Informe o {} valor ==> '.format(c)))
    if num%2==0:
        soma= (soma+num)
        contador= (contador+1) 
        
print('Você informou {} números, e a soma entre eles é igual à ==> {}'.format(contador, soma))
   
    