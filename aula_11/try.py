import statistics 


#Exercício 1:
#Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.

def inserir():
    try:
        n = int(input('Digite um numero'))
        
    except ValueError as erro:
        print('Erro de Digitação',erro)
   



# Exercício 2:
# Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação  -  ZeroDivisionError.

try:
    y = int(input('Digite um numero'))
    x = int(input('Digite outro numero'))
    print(y/x)
except ZeroDivisionError as erro :
    print('Erro de Digitação',erro)



# Exercício 3:
# Crie uma função que aceite uma lista e um índice como entrada e retorne o elemento naquele índice.
# Manipule a exceção caso o índice seja inválido(caso imprima um indice que não exista na lista).


def divisao(lista):
    try:
        a = int(input("Digite um indice para sua lista"))
        print(lista[a])
    except IndexError as erro:
        print('Erro de Digitação',erro)
lista =[1,2,3]

divisao() 


# Exercício 4:
# Crie uma função que divida dois números e manipule a exceção caso o divisor seja zero.

try:
    nu= int(input('Digite um numero'))
    z= 15
    print(nu/z)
except ZeroDivisionError as erro:
    print("A divisão não ser por zero",erro)

    