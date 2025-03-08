numeros = range(1, 6)  # Cria a sequência de números de 1 a 5
print ('Cria a sequência de números de 1 a 5')
print(list(numeros))  # Converte o range para lista e imprime
print ('Some estes  numeros')
soma = sum(numeros)# soma automatica
print (soma)
print ('Qual o menor e o maior numero ')
min = min(numeros)  # Isso irá retornar 1
max = max(numeros)
print ('o menor é,{}, e o maior é,{}'.format(min,max))
numero = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print ('Oa numeros 3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5 estão desorganizadas arume:')
numero_o = sorted(numero)
print (numero_o)
print
minha_lista = [1, 2, 3, 4, 5]
primeiro_elemento = minha_lista[0]
print(primeiro_elemento)  # Isso imprimirá 1
minha_lista.append(6)
print(minha_lista)
minha_lista.remove(3)  # Isso removerá o elemento 3 da lista
del minha_lista[4]  # Isso removerá o quinto elemento (índice 4) da lista
print(minha_lista)
