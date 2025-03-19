import random


for i in range(1,4) :
    numero =  random.randint(1,5)
    chute =  int(input('Digite um numero da sorte: '))
    if chute == numero:
        print('Você acertou, o nº é ', numero)
        break
    else:
        print('Você errou, o nº é', numero)
        



# desafio CISCO 
# 3.2.14           
for i in range(3):
    print( '[]' * (-i) + '[]'  * (1*i + 1) )