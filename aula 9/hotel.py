# Sistema de Reservas de Hotel:
# Você foi contratado(a) para desenvolver uma parte do sistema de um hotel. O objetivo é criar um sistema que gerencie reservas de quartos e o pagamento das diárias
# Cadastro de Cliente
print('Olá seja Bem Vindo Ao Aconchego Hotel.')
reserva = input('Gostaria de fazer uma reserva. s/n ')
quartos = {
     1 :['Simples', 100],
     2 :['Duplo'  , 150],
     3 :['Luxo'   , 250],
}
if reserva == 's' :
    nome = input('Por favor, digite seu nome: ')
    idade = int(input("Qual a sua idade: "))
if idade < 18 :
    print ('Voce não pode reservar um quarto, chame um responsavel.')
else:
    print('Foi cadastrado com Sucesso')
    print('Escolha  um de nossos quartos:',quartos)
    quarto = input('')
    if quar
    dias = int(input('Quandos dias será sua reserva: '))
    total = quartos * dias
    print(nome,' escolha  o quarto',quartos,' e vai se ospedar por ',dias,' pagando o valor total de ',total)



