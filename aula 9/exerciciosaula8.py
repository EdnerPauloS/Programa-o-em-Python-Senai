import random

#EXERCÍCIOS: 

# 1-Peça para o usuário digitar um número, verifique se um número é positivo, negativo ou zero.

# numero = int(input('Digite um numero: '))
# if numero > 0 :
#     print ('É possitivo')
# elif numero < 0 :
#     print ('É negativo')
# else:
#     print ('É Zero')

# 2-Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com base na idade.
# idade = int(input('Digite a sua Idade: '))
# if  idade >= 16 and idade < 18 :
#     print ('O voto é facultativo')
# elif idade >= 18 and idade <= 65 :
#     print ('O voto é obrigatorio')
# elif idade > 65 :
#     print ('O voto é facultativo')
# else:
#     print ('Menor não pode votar')

# 3- Declara uma variável com um número qualquer, determine se um número é par ou ímpar.
# numero = int(input('Digite um numero: '))

# if numero % 2 == 0:
#     print('E um numero Par')
# else:
#     print('É um numero Impar')


# 4-Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo é equilátero, isósceles ou escaleno
# Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida. 
# Um triângulo é chamado de isósceles se dois lados possuem a mesma medida. 
# Um triângulo é chamado de escaleno se todos os lados possuem medidas diferentes.

# numero1= int(input('Digite um numero: '))
# numero2 = int(input('Digite um numero: '))
# numero3 = int(input('Digite um numero: '))

# if numero1 == numero2 == numero3:
#     print(' E um triângulo equilatero ')
# elif numero1 == numero2 != numero3  or numero1 != numero2 == numero3 or numero1 == numero3 != numero2:  
#     print(' E um triângulo isosceles ')
# else:
#     print(' E um triângulo escaleno ')


# 5- Determine se um número é múltiplo de 5 e 7.
# numeros = int(input("Digite um numero: "))

# if numeros % 5 == 0 and numeros % 7 == 0:
#     print(numeros,'é multiplo de 5 e 7 ')
# else: 
#    print(numeros,' não é multiplo de 5 e 7')    


# 6- Verifique se um número é positivo e maior que 10

# numero = int(input('Digite um numero: '))
# if numero > 0 and numero > 10 :
#     print ('o numero ',numero,' é possitivo e maior que 10')
# else:
#     print('O numero ',numero,' não é positivo ou maior que 10  ')

# 7-Verifique se um número é divisível por 3 ou 5.

numeros = int(input("Digite um numero: "))

if numeros % 3 == 0 or numeros % 5 == 0:
    print(numeros,'é divisivel por 3 ou 5 ')
else: 
    print(numeros,' não é divisivel por 3 ou 5 ')



