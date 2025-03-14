#cadastrar-se
print('Ola seja Bem Vindo.')
nome = input("Digite o seu nome: ")
email = input("Qual o seu email: ")
telefone = input("Qual o seu telefone: ")
print()
print()
print('Ola, ',nome,'seja Bem Vindo.')
print('Seu email é: ',email)
print('E seu telefone é :',telefone)
print('Esta cadastrado com Sucesso')
print()
escolha = input('Gostaria de compra nossos produtos, s/n ')
#comprar um produto 
produtos = {
     1 :[ 'celular'    , 1500],
     2 :['televisao'   , 1850],
     3 :['notebook'    , 2500],
     4 :['microSystem' , 4000] 
}
#descobrir o valor total 

if escolha == 's' :
    print("Este são os nossos Produtos :",produtos)
    escolha1 = int(input())
    escolha2 = int(input())
    escolha3 = int(input())
    escolha4 = int(input())
    carrinho=[]
    valores =[]

    carrinho = [produtos[escolha1][0], produtos[escolha2][0], produtos[escolha3][0], produtos[escolha4][0]]
    valores = [produtos[escolha1][1], produtos[escolha2][1],produtos[escolha3][1],produtos[escolha4][1]]
    SOMA = sum(valores)
    # Pagar 
    print(f'''
    .................................
        Você escolheu estes produtos
    .................................
        
        1 - {carrinho[0]} R$ {valores[0]:.2f}
        2 - {carrinho[1]} R$ {valores[1]:.2f}
        3 - {carrinho[2]} R$ {valores[2]:.2f}
        4 - {carrinho[3]} R$ {valores[3]:.2f}

    .................................
        O Total é : R$ {SOMA:.2f}
    .................................

    ''')
    print ('Qual a forma de pagamento: ')
    pagamento = input('credito / pix / debito: ')
    if pagamento == 'credito':
        print('Voce pagara com ',pagamento )
        print('.................................')
        print('.........VOLTE SEMPRE............')
    elif pagamento == 'pix':
        print('Voce pagara com ',pagamento )
        print('.................................')
        print('.........VOLTE SEMPRE............')
    elif pagamento == 'pix':
        print('Voce pagara com ',pagamento )
        print('.................................')
        print('.........VOLTE SEMPRE............')
    else:
        print('Voce não escolheu uma forma de pagamento')
        print('.................................')
        print('.........VOLTE SEMPRE............')
else:
    print('Fim do programa \n VOLTE SEMPRE')




