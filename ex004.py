x= input('Digite algo: ')
print(x,'É do tipo primitivo: ',type(x))
print(x,'possui apenas números',x.isnumeric())
print(x,'possui apenas letras?',x.isalpha())
print(x,'possui letras ou números?',x.isalnum())