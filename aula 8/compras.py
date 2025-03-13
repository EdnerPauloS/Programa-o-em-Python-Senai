produtos = {
    "livro": 50.0,
    "tablet": 250.0,
    "fones": 25.0
}

print (' Bem vindo a suas compras On-line')
print (' Escolha nossos produtos')
print (produtos)
print ('Escolha dentre essas opções')
escolha1 = input()
escolha2 = input()
escolha3 = input()
escolha4 = input()
carrinho=[]
valores =[]

carrinho +=(escolha1,escolha2,escolha3,escolha4)

valores = [produtos[escolha1], produtos[escolha2], produtos[escolha3],produtos[escolha4]]
SOMA = sum(valores)

 
print(f'''
.................................
Você escolheu estes produtos
.................................
      
1 - {carrinho[0]} R$ {valores[0]:.2f}
2 - {carrinho[1]} R$ {valores[1]:.2f}
3 - {carrinho[2]} R$ {valores[2]:.2f}
4 - {carrinho[3]} R$ {valores[3]:.2f}

.................................
O Total é :
.................................
R$ {SOMA:.2f}

VOLTE SEMPRE
''')



# loja = {
# 'fone':100.00,
# 'livro x': 50.00,
# 'Tablet':5000.00
# }




# prod1 = input('Digite o produto')
# prod2 = input('Digite o produto')
# prod3 = input('Digite o produto')
# prod4 = input('Digite o produto')


# lista_prod = []
# lista_valores = []


# lista_prod.extend([prod1,prod2,prod3, prod4])
# lista_valores +=(loja[prod1], loja[prod2], loja[prod3], loja[prod4])


# soma = sum(lista_valores)
# print('Produtos:', lista_prod)
# print('...'*2)
# print('R$', soma)
