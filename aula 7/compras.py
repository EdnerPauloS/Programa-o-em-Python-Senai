produtos = {
    "Nada": 0.00,
    "Livro": 50.0,
    "Tablet": 250.0,
    "Fones de Ouvido": 15.0
}
carrinho=[]
valores =[]

carrinho1= ('''
0 - Nada,
1 - livro,
2 - tablet,
3 - fones de ouvido
     
''')

print (' Bem vindo a suas compras On-line')
print (' Escolha nossos produtos')
print (produtos)
print (carrinho1)
print ('Escolha dentre essas opções')
escolha1 = int(input())
escolha2 = int(input())
escolha3 = int(input())

produtos_lista = ["Nada", "Livro", "Tablet", "Fones de Ouvido"]

produto1 = produtos_lista[escolha1]
produto2 = produtos_lista[escolha2]
produto3 = produtos_lista[escolha3]

carrinho = [produto1, produto2, produto3]
valores = [produtos[produto1], produtos[produto2], produtos[produto3]]
 
print(f'''
.................................

1 - {carrinho[0]} R$ {valores[0]:.2f}
2 - {carrinho[1]} R$ {valores[1]:.2f}
3 - {carrinho[2]} R$ {valores[2]:.2f}

.................................

R$ {SOMA:.2f}

VOLTE SEMPRE
''')

