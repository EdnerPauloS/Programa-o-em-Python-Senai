# EXERCÍCIOS:
# numero = 20
# match numero:
#     case 0 :
#         print('é 1')
#     case 1 :
#         print('é 1')
#     case 2 :
#         print('é 2')
#     case _:
#         print('DESCONHECIDO')

# 1: Verificando se o número é par ou ímpar
# numero1 = int(input('Digite um número: '))
# match numero1:
#     case a if a % 2 == 0:
#         print('Divisor de 2')
#     case x if x % 3 == 0:
#         print('Divisor de 3')
#     case _:
#         print('Impar')
        
# 2: Verificando se um número é positivo, negativo ou zero
# numero2 = int(input('Digite um número: '))
# match numero2:
#       case x if x > 0:
#         print('É um numero positivo')
#       case x if x == 0:
#         print('É Zero')
#       case x if x < 0:
#         print('É um numero negativo')
    
# 3: Verificando se uma string é vazia ou não

texto = str(input('Digite algo que vc gosta: '))

def check_with_match(value):
    match value:
            case str():
                print('É um texto é uma String')
            case _:
                print("Desconhecido")

check_type_with_match

# 4: Verificando se um número é maior, menor ou igual a 10
# 5: Classificando uma idade em faixas etárias - criança, jovem, adulto, idoso        
