cont= 0

while True:
    num= int(input('Digite um número para saber sua tabuada ==> '))
    if (num<0):
        break
    for cont in range(0, 10+1):
        tabuada= (num*cont)
        print(f' {num} X {cont} = {tabuada}')
        