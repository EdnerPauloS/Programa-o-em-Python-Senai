#conjunto
# que configura o conjunto e o set automaticamento
# principla caraquiteristica e {}

conjunt = set(range(1,11))
c = {10,3,6,6,6}
print (conjunt)
print(c)
print()
print()

conjunto1 = {1, 2, 3, 4}
conjunto2 = {3, 4, 5, 6}
conjunto3 = {7,8,9,10}

# União
uniao = conjunto1 | conjunto2  # ou conjunto1.union(conjunto2)
print(uniao)  # Saída: {1, 2, 3, 4, 5, 6}

# Interseção
intersecao = conjunto1 & conjunto2  # ou conjunto1.intersection(conjunto2)
print(intersecao)  # Saída: {3, 4}

# Diferença
diferenca = conjunto1 - conjunto2  # ou conjunto1.difference(conjunto2)
print(diferenca)  # Saída: {1, 2}

# Diferença simétrica
dif_simetrica = conjunto1 ^ conjunto2 ^ conjunto3 # ou conjunto1.symmetric_difference(conjunto2)
print(dif_simetrica)  # Saída: {1, 2, 5, 6}

# Verificar subconjunto
print({1, 2}.issubset(conjunto1))  # Saída: True
print(conjunto1.issuperset({1, 2}))  # Saída: True



# Criando um conjunto com chaves {}
conjunto1 = {1, 2, 3, 4, 5}
print(conjunto1)  # Saída: {1, 2, 3, 4, 5}

# Criando um conjunto com a função set()
conjunto2 = set([1, 2, 3, 4, 5])
print(conjunto2)  # Saída: {1, 2, 3, 4, 5}

#Adicionando Elementos
#Para adicionar elementos a um conjunto, utilize o método add().


conjunto = {1, 2, 3}
conjunto.add(4)
print(conjunto)  # Saída: {1, 2, 3, 4}

#Removendo Elementos
#Para remover um elemento de um conjunto, utilize os métodos remove() ou discard(). A diferença entre eles é que remove() gera um erro se o elemento não estiver presente no conjunto, enquanto discard() não gera erro.


conjunto = {1, 2, 3, 4}
conjunto.remove(3)
print(conjunto)  # Saída: {1, 2, 4}

conjunto.discard(2)
print(conjunto)  # Saída: {1, 4}

conjunto.discard(5)  # Não gera erro se o elemento não existir
print(conjunto)  # Saída: {1, 4}
