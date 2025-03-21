# # Exercícios com funções:
# #1 CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS.***
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def teste(numeros):
#     for numero in numeros:
#         if numero % 2 == 0: 
#             print (f'Este numeros é par, {numero}')
#         else:
#             print (f'Este numeros é impar, {numero}')

# teste(numeros)

# #2 CRIE UM AFUNÇÃO PARA MULTIPLICAR 3 NUMEROS.***

# x = 3
# y = 5 
# z = 6

# def multiplica():
#       resultado =  x * y * z
#       print (resultado)
      
# multiplica()     

#3 CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.***

# numero = int(input('Escolha um numero: '))
# elevado = int(input('Escolha um numero para elevalo: '))


# def potencia():
#     p = numero ** elevado
#     print(f'O numero {numero} elevado a potencia de {elevado} é {p}')
    
# potencia()

# #4 CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO  DIGITAR, 18 ANOS***
# print ('Digite seu nome e sua idade siga o exemplo abaixo:')
# print ('Paulo Dias 42 anos')
# name = input('Nome: ')
# age = input('Idade: ')

# def maior():
#     if age == '18 anos':
#         print(f'Parabéns {name}, você é tem 18 anos e esta na melhor parte da vida')
#     else:
#         print(f'{name},infelizmente você não atingio a meta')
        
# maior()

# #5 DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.***

 
# def nascimento():
#     print ('Digite seu nome e em seguida a sua idade')
#     nome = input("Nome: ")
#     ano_nasc = int(input("Digite o ano que vc nasceu: "))
#     mes_nasc = int(input("Digite o mes que vc nasceu: "))
#     mes_atual = int(input("Digite o mes em que estamos: "))
#     ano = 2025
#     if idade  :
#         idade = ano - ano_nasc
#         print(f'Parabéns {nome}, você tem {idade} anos')
#     else:
#         print(f'{nome},infelizmente você não é maior de 18 anos')

#     if mes_nasc <= mes_atual
#         idade = (ano-1)- ano_nasc
#         print idade
        
# maioridade()


#6 DESENVOLVA UM AFUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999

def verificar():
    anos_lista=[1958,1962,1994,1998,2002]
    ano = int(input('Digite o ano que você acha que o brasil ganhou: '))
    if ano in anos_lista:
        print('O brasil foi campeão em ',ano)
    else:
        print('O brasil  nâo foi campeão em ',ano, '. Tente Novamente ')
             
verificar()


#7 DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA, SANDUICHE, SORVETE.***


# produtos= {
#     SALADA, 50,
#     MACARRONADA, 
#     SANDUICHE, 
#     SORVETE
    
# }