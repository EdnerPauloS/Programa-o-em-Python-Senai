lista =[]# lista vazia
lista = [1,10,5,3,20,'a',True,5.2]
#        1  2 3 4  5  6    7   8
print ('ESTA E A LISTA ORIGINAL', lista)
lista.append('teste')
lista.insert(6,'Olá')
lista+=(100,200,300,2500,250)
lista.extend([500,200,30,20,20])
print (lista)
lista.pop(7)
lista.pop()
print (lista)

del lista[5]
lista.remove('teste')
lista.remove('Olá')
print (lista)

lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)
maximo = max(lista)
print(maximo)

lista2 = list(range(0,100,2))
lista2.sort(reverse=True)
print(lista2)
        

lista_f = [5.3,5.2,8.4,10.8]
lista_i = [1,5,6,5,32,45]
lista_b = [True,False,True,True]
list_str =['456','fhjaasd','6466']

lista[0] = 100
lista[6] = 200
lista[2] = lista[1]*2

