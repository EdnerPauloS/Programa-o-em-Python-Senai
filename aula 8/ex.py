# import random

# numero_aleatorio = random.randint(1,10)
# meu_chute  =  int(input('Declare seu chute'))

# if numero_aleatorio == meu_chute:
#     print('Sensacional você acertou em cheio!', numero_aleatorio)
# elif numero_aleatorio > meu_chute:
#     print('Você esta quase lá, o número é maior, tente novamente')    
# elif numero_aleatorio < meu_chute:
#     print('Você esta quase lá, o número é menor, tente novamente')       
# else:
#     print('Errou Feio!', numero_aleatorio)    


# number  =  0
# if number > 2:
#     print('é maior que 2 ')

# if number == 3:
#     print('é 3 ')

# if number < 0:
#     print('é negativo ')

# if number >200:
#     print('é maior que 200 ')    

# # else: 
# #     print('É menor')    

# # composta  
    
# nome  =  input('Digite seu nome: ')
# lista  =  ['Ana','José','Caio']


# if nome in lista:
#     print('Seja bem vindo(a), cliente', nome)
# elif nome == 'Julia':
#     print('Seja bem vinda cliente Premium ', nome)
# elif nome  == '':
#      print('Esta vazio digite novamente')    
# else:    
#     print('Seja bem vindo(a) novo(a) cliente', nome)

# OUTROS EXEMPLOS: 

# meu_carrinho = []
# total_valores = []
# produtos=  ['arroz', 'feijão', 'ervilha']
# valores =  [20.0,18.0,5.]

# produto1 = input('Digite o produto 1: ')
# produto2 = input('Digite o produto 2: ')
# produto3 = input('Digite o produto 3: ')

# if (produto1, produto2, produto3) == (produtos[0], produtos[1], produtos[2]):
#     meu_carrinho += (produtos[0], produtos[1], produtos[2])
#     print(meu_carrinho)
# if (produto1, produto2, produto3) != produtos:
#     print('Não existe o produto')

# if produto1 in produtos or produto2 in produtos or produto3 in produtos:
#    meu_carrinho.append(produto1)
#    meu_carrinho.append(produto2)
#    meu_carrinho.append(produto3)

# if produto1 in produtos:
#    meu_carrinho.append(produto1)
#    print(meu_carrinho)
#    meu_carrinho2 = meu_carrinho
# if produto2 in produtos:
#    meu_carrinho2.append(produto2)
#    print(meu_carrinho2)
#    meu_carrinho3 = meu_carrinho2
# if produto3 in produtos:
#    meu_carrinho3.append(produto3)
idade = 18
if idade >= 18:
    print("Você é maior de idade.")

nota = 85
if nota >= 90:
    print("Ótimo desempenho!")
elif nota >= 70:
    print("Bom desempenho.")
else:
    print("Melhorar na próxima.")

numero = 7
if numero % 2 == 0:
    print("O número não é par.")
else:
    print("O número impar.")

    senha  = 123
login = 'bea@'

my_login =  input('Digite o login')
my_senha  = int(input('Digite a sua senha'))

if my_login == login and my_senha == senha:
    lista =  ['arroz', 'feijão', 'salada', 'ovos'] # string
    meu_carrinho = []
    meu_total = []
    valores = [10.00,5.0,4.40,12.0] # float
    print('PRODUTOS')
    print(f'''digite o ID do produto:
    0 - Arroz
    1 - Feijão
    2 - Salada
    3 - Ovos            
    ''')

    escolha  =  input('Deseja fazer o pedido? s/n')
    if escolha == 's':
        produto1 = int(input('>>'))
        produto2 = int(input('>>'))
        produto3 = int(input('>>'))
        meu_carrinho += (lista[produto1],lista[produto2],lista[produto3] )
        meu_total +=(valores[produto1],valores[produto2], valores[produto3])
        print('Carrinho:', meu_carrinho)
        print('Total')
        soma = sum(meu_total)
        print(f'R$, {soma:.2f}')
        print(f'''
    1 - PIX
    2 - CC
    3 - CD                    

    ''')
        forma_pag =  input('Digite a forma de pagamento')
  
        if forma_pag:
            print('Pagamento efetuado com sucesso volte sempre!')  
    else:
        print('Pedido cancelado')
else:
    print('dados incorretos - Digite novamente')


