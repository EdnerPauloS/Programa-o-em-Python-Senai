# Faça um programa, utilizando while,
# que mostre na tela os números de 0 a 1000.

# contador = 0
# while contador <= 1000:
#      print("Número:", contador)
#      contador += 1
     
     
     
#  Faça um sistema, utilizando while e listas, que permita o usuário
#  escrever o nome de 10 pessoas e os mostre na tela.

escolha = input('Preencha nosso formulario com 10 clientes. s/n')
dicionario = {'nome': [], 'email':[] }
while escolha == 's' or escolha == 'sim' :
    print('Preencha o formulário: ')
    
    print(' Digite seu nome:')
    nome = input('nome - ')
    print(' Digite seu email:')
    nome = input('email - ')
    dicionario['nome'].append(nome)
    dicionario['email'].append(email)
    print(dicionario)
else:
    print('Você não quis preencher tosdos os clientes')