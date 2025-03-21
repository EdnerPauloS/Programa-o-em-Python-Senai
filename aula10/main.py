from funcoes import *

def banco():
    saldo = 5000
    while True:
        print("Seja bem vindo(a): ")
        print("Escolha um operação:")
        escolha = input('| 1 saque | 2 Deposito | 3 Extrato |')
        if escolha == '1':
            valor_de_saque = float(input('Saque em  dinheiro R$: '))
            saldo = saque(saldo,valor_de_saque)
            print('Em sua conta tem R$',saldo) 
        elif escolha == '2':
            valor_de_deposito = float(input('Deposito em  dineiro R$: '))
            saldo = deposito(saldo,valor_de_deposito)
            print('Em sua conta tem R$',saldo) 
        elif escolha == '3':
            saldo = extrato(saldo)
            print('Em sua conta tem R$',saldo) 
        else:
            print('Você nao digitou um valor valido')
            
        continuar = input('Deseja realizar outra operação? (s/n): ').strip().lower()
        if continuar != 's':
            print("Saindo do sistema. Até logo!")
            break  
        
banco()
        