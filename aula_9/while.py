       
# loop while  -  contador


# c =  10
# while c >0:
#     print(c)
#     c -= 1


# while infinito


# n = 100
# while n > 0:
#     n = n -1
#     print('Olá mundo', n)



#  strings 



# pergunta = input('Digite a sua escolha:  sim ou não')


# for n in range(1,10):
#     print(n)



# while pergunta == 'sim':
#     print('Preencha o formulário: ')
#     print('nome:')
#     nome = input('Nome - ')
#     print('nome:', nome)
#     pergunta = input('Deseja continuar sim/não')



# else:
#     print('obrigada volte sempre')

import random

chances = 3
while chances > 0 :
    numero =  random.randint(1,5)
    chute =  int(input('Digite um numero da sorte: '))
    if chute == numero:
        print('Você acertou, o nº é ', numero)
        break
    else:
        print('Você errou, o nº é', numero)
        chances = chances - 1
        print('Quantidade de chances', chances)  
        print('Chances esgotadas.')
        print('Você perdeu o jogo!!!! ;(')  





# dicionario = {'nome': [], 'email':[],'senha':[]}


# numero = int(input('digite a quantidade de cadastros: '))
# print('cadastre-se: ')
# for n in range(0,numero):
#     nome = input('nome: ')
#     email = input('E-mail: ')
#     senha = input('Senha: ')
#     dicionario['nome'].append(nome)
#     dicionario['email'].append(email)
#     dicionario['senha'].append(senha)
#     print(dicionario)


# dados_usuario = dicionario


# email_usuario = input('digite o email')
# senha_usuario = input('digite a senha')
# carrinho = []
# while email_usuario in dicionario['email'] and senha_usuario in dicionario['senha']:
#     escolha = input('Deseja fazer o pedido?')
#     while escolha == 's' or escolha =='sim' or escolha =='S' or escolha == 'SIM':
#         produtos = ['a','b','c','d']
#         print('produtos', produtos)
#         meu_prod  = int(input('digite o indice 0 1 2 3 '))
#         carrinho.append(produtos[meu_prod])
#         print('CARRINHO: ', carrinho)
#         escolha = input('Deseja continuar? s/n')
#     else:
#         print('Obrigada volte sempre!!')   
#         break 
# else:
#     print('Acesso negado dados incorretos! ')        