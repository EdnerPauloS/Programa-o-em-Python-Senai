# Exercícios com funções:
#1 CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS.***
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def teste(numeros):
    for numero in numeros:
        if numero % 2 == 0: 
            print (f'Este numeros é par, {numero}')
        else:
            print (f'Este numeros é impar, {numero}')

teste(numeros)

#2 CRIE UM AFUNÇÃO PARA MULTIPLICAR 3 NUMEROS.***

x = 3
y = 5 
z = 6

def multiplica():
      resultado =  x * y * z
      print (resultado)
      
multiplica()     

#3 CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.***

numero = int(input('Escolha um numero: '))


def potencia():
    p = numero ** 2
    print(f'O numero {numero} elevado a potencia de 2 é {p}')
    
potencia()

#4 CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO  DIGITAR, 18 ANOS***
print ('Digite seu nome e sua idade siga o exemplo abaixo:')
print ('Paulo Dias 42 anos')
name = input('Nome: ')
age = input('Idade: ')

def maior():
    if age == '18 anos':
        print(f'Parabéns {nome}, você é tem 18 anos e esta na melhor parte da vida')
    else:
        print(f'{nome},infelizmente você não atingio a meta')
        
maior()

#5 DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.***

print ('Digite seu nome e em seguida a sua idade')
nome = input("Nome: ")
idade = int(input("Idade: "))


def maioridade():
    if idade > 17:
        print(f'Parabéns {nome}, você é maior de 18 anos')
    else:
        print(f'{nome},infelizmente você não é maior de 18 anos')
        
maioridade()


#6 DESENVOLVA UM AFUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999***

#7 DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA, SANDUICHE, SORVETE.***