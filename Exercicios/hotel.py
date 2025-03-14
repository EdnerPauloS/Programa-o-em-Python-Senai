# Meu exercicio
# Sistema de Reservas de Hotel:
# Você foi contratado(a) para desenvolver uma parte do sistema de um hotel. O objetivo é criar um sistema que gerencie reservas de quartos e o pagamento das diárias
# Cadastro de Cliente
print('Olá seja Bem Vindo Ao Aconchego Hotel.')
reserva = input('Gostaria de fazer uma reserva? s/n ')

# Definindo os quartos e preços
quartos = {
    1: ['Simples', 100],
    2: ['Duplo', 150],
    3: ['Luxo', 250],
}

if reserva == 's':
    nome = input('Por favor, digite seu nome: ')
    idade = int(input("Qual a sua idade: "))

    if idade < 18:
        print('Você não pode reservar um quarto, chame um responsável, por favor.')
    else:
        print('Cadastro realizado com sucesso!')
        print('Escolha um de nossos quartos:')
        print('1 - Simples: R$100')
        print('2 - Duplo: R$150')
        print('3 - Luxo: R$250')

        quarto = int(input('Digite o número do quarto que deseja reservar: '))

        if quarto in quartos:
            nome_quarto, preco = quartos[quarto]
            dias = int(input('Quantos dias será sua reserva? '))
            total = preco * dias
            print(f'{nome}, você escolheu o quarto {nome_quarto} e ficará hospedado por {dias} dias, pagando o valor total de R${total}.')
        else:
            print('Opção de quarto inválida, tente novamente escolhendo uma das opções corretas.')
else:
    print('Obrigado por visitar o Aconchego Hotel. Até a próxima!')

#Feito pela professora

# cliente_nome1 = input('Nome:  ')
# cliente_idade1 = int(input('Idade: ')) 
# cliente_nome2 = input('Nome:  ')
# cliente_idade2 = int(input('Idade: ')) 


# lista_quartos =  ['SIMPLES', 'DUPLO', 'LUXO']
# lista_valores_quartos = [100.0,150.0,250.0]


# print('escolha a partir do código do quarto 0 - 1 - 2  ', lista_quartos)


# escolha_quarto1 = int(input('Escolha o quarto Cliente 1: '))
# escolha_quarto2 = int(input('Escolha o quarto Cliente 2: ')) 


# dias_quat1 = int(input(f'Digite os dias {cliente_nome1}'))
# dias_quat2 = int(input(f'Digite os dias {cliente_nome2}'))


# calc1 = lista_valores_quartos[escolha_quarto1] * dias_quat1
# calc2 = lista_valores_quartos[escolha_quarto2] * dias_quat2


# print('O Usuário ', cliente_nome1, 'escolheu o quarto',lista_quartos[escolha_quarto1])
# print('O Usuário ', cliente_nome2, 'escolheu o quarto',lista_quartos[escolha_quarto2])


# print('Total cliente',cliente_nome1, 'R$', calc1)
# print('Total cliente',cliente_nome2, 'R$', calc2)
