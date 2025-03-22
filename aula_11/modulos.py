import random  


def gerar_numero_aleatorio():
    
    return random.randint(5, 10)
gerar_numero_aleatorio()

def gerar_numero_aleatorio2():
    
    n = random.randint(1, 10)
    nu = random.randint(11, 20)
    num = random.randint(21, 30)
    print(f"Os numeros serão {n} , {nu}, {num} ")
gerar_numero_aleatorio2()    

def aleatorio():
    nume = list(range(10, 30))  
   
aleatorio()

def contagem():
    for numero in range(11, 0, -1):
        print(numero)
        if numero == 1:
            print('Fogo!')

contagem()