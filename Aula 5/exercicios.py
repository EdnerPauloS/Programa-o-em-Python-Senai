
nome = input("Qual o seu nome: ")
cumprimento = "Seja Muito Bem Vindo "
senha = int(input("Digite um a senha: "))





print(cumprimento, nome,'Sua senha é',senha)
print(f'{cumprimento} {nome} Sua senha é {senha}')
print(cumprimento + " "+ nome+ " " + 'Sua senha é',senha )
print(cumprimento, nome, 'Sua senha é {}'.format(senha))
print(cumprimento, nome, 'Sua senha é %s'%(senha))

# CONCATENAR = JUNTAR DADOS 
# virgula 
print('Olá',nome)


# sinal de mais (precisam ser o mesmo tipo de dado)


print('olá '+ nome)


# função format 


print('olá {}'.format(nome))



# % com a porcentagem


print('olá %s '%(nome))



# f string



print(f'olá {nome}')
