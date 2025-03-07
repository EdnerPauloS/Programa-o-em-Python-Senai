#pular linha

print ('test unitario')
print
print ('test  unitario')       
print ('test \nunitario')
print ('''
test unitario
''')       
# https://docs.python.org/pt-br/3.13/library/functions.html#print
print ('teste',"teste2", end = '--', sep= '==' )
print
palavra = ' teste 2025'
print (len(palavra))
# conta quantas palavras tem a frase
print
#variavel 1 dado
# lista varios dados
lista = [2,3,4,5,6,7,8,9,10]
lista2 = [2,4,6,8,10,3,5,7,9 ]
numeros = list(range(0,21,2))
print (lista)
print
print(numeros)
soma=(sum(lista))
print (soma)

maior = max(lista)
menor = min(lista)
print (' O maior é ',maior,'e o menor é ',menor)

lista2.sort()
print (lista2)
lista2.sort(reverse=True)
print (lista2)
