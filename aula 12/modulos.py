import random  


# def gerar_numero_aleatorio():
    
#     return random.randint(5, 10)
# gerar_numero_aleatorio()

# def gerar_numero_aleatorio2():
    
#     n = random.randint(1, 10)
#     nu = random.randint(11, 20)
#     num = random.randint(21, 30)
#     print(f"Os numeros serão {n} , {nu}, {num} ")
# gerar_numero_aleatorio2()    

# def aleatorio():
#     nume = list(range(10, 30))  
   
# aleatorio()

# def contagem():
#     for numero in range(10, 0, -1):
#         print(numero)
#         if numero == 1:
#             print('Fogo!')

# contagem()

# def soma (n_p):
#     soma = 0     
#     for n in range(n_p,11,2):
#         print(n)
#         soma = soma + n 
# soma(2)      


def tabuada(meu_numero):
    lista= list(range(0,11))
    for n in lista:
        calc = n * meu_numero 
        print(calc)