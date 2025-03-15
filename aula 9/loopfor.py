

#for variável in sequência:
# Código a ser executado para cada item 
#na sequência

# for numero in range(1,11):
#     print(numero)

# lista  =  [1,2,3,4,5,6,7,8,9,10,11]
# for numero in lista:
#     print(numero)    


# tuplas =  (103,6,6,6,4)
# for numero in tuplas:
#     print(numero)    

# dictionary = {'nome': 'Carlos', 
#             'sobrenome':'Augusto',
#             'endereco':'Rua 25, Jd.x',
#             }
# for chave, valor in dictionary.items():
#     print(chave, valor)
   

# conjuntos = {1020, 3, 3, 3, 56, 'hj'}

# for elemento in conjuntos:
#     print(elemento)

# frutas = ["maçã", "banana", "laranja"]
# for fruta in frutas:
#     print(fruta)

# palavra = "Python"
# for letra in palavra:
#     print(letra)

# for numero in range(1, 6):
#     print(numero)

# pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
# for chave, valor in pessoa.items():
#     print(chave, ":", valor)

# # Matriz
# matriz = [[1, 2, 3], [7, 8, 9], [4, 5, 6]]

# # Iterando sobre a matriz e imprimindo os elementos
# for linha in matriz:
#     for elemento in linha:
#         print(elemento)

# # Função para calcular o produto e adicionar à lista
# def calculo_do_produto(x):
#     lista = []
#     for n in range(1, 11):
#         resultado = x * n  # Produto de x com o número n
#         lista.append(resultado)  # Adiciona o resultado à lista
#         print(resultado)  # Imprime o resultado
#     print(lista)  # Imprime a lista completa ao final

# # Exemplo de chamada da função
# calculo_do_produto(5)  # Pode substituir 5 por qualquer outro número

# variavel_texto = 'python'


# for n in variavel_texto:
#     print(n) 


# dicionario = {
# 'a':10,
# 'b':20,
# 'c':30
# }


# k1 = []
# v1 = []
# for k, v in dicionario.items():
#     k1.append(k)
#     v1.append(v)
#     print(v, k)
# print(k1)
# print(v1)



# # QUARTOS COM LOOP
# # Listas e dicionários
# quartos = ['SIMPLES', 'DUPLO', 'LUXO']
# precos = [100.0, 150.0, 250.0]
# descontos = [0.2, 0.5, 0.6]

# # Armazenamento de dados dos clientes
# clientes = []
# escolhas_quartos = []
# meus_valores = []

# print('''Sejam bem-vindos,
# Cadastre-se e escolha o ID do quarto:
# SIMPLES(0), DUPLO(1), LUXO(2)''')

# # Quantidade de hóspedes
# quantidade_hospede = int(input('Quantidade de Hospedes: '))

# # Processamento dos dados de cada cliente
# for n in range(quantidade_hospede):
#     # Coletando os dados do cliente
#     nome = input(f'Nome do hóspede {n+1}: ')
#     idade = int(input(f'Idade do hóspede {n+1}: '))
#     quarto_id = int(input('Escolha o ID do quarto (0, 1, 2): '))
#     dias = int(input('Quantidade de dias de hospedagem: '))
    
#     # Armazenando os dados
#     clientes.append(nome)
#     escolhas_quartos.append(quarto_id)
#     meus_valores.append(precos[quarto_id])

#     # Cálculos
#     valor_total = precos[quarto_id] * dias
#     desconto = valor_total * descontos[quarto_id]
#     total_a_pagar = valor_total - desconto

#     # Exibindo as informações de forma mais clara
#     print(f'\nDetalhes do Hóspede {n+1}:')
#     print(f'Cliente: {nome}')
#     print(f'Idade: {idade}')
#     print(f'Quarto Escolhido: {quartos[quarto_id]}')
#     print(f'Preço por Dia: R${precos[quarto_id]:.2f}')
#     print(f'Quantidade de Dias: {dias}')
#     print(f'Valor Total: R${valor_total:.2f}')
#     print(f'Desconto: R${desconto:.2f}')
#     print(f'Total a Pagar: R${total_a_pagar:.2f}')
#     print('-' * 40)

# # Resumo final
# print('\nResumo dos Hóspedes:')
# for i in range(quantidade_hospede):
#     print(f'{clientes[i]} escolheu o quarto {quartos[escolhas_quartos[i]]} por R${meus_valores[i]:.2f} por {dias} dias.')




  
                        
             

