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

