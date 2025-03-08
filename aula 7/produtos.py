#loja de roupas
lista_prod =['meias','camisas','blusas','calças']
valores = [10.25,100.0,250.0,300.20]
print('Produtos disponiveis')
print(lista_prod)
print('-----'*10)
meu_carrinho =[]
meu_total = []
prod1 = int(input('Escolha a partir do indece: '))
prod2 = int(input('Escolha a partir do indece: '))
prod3 = int(input('Escolha a partir do indece: '))
prod4 = int(input('Escolha a partir do indece: '))
prod5 = int(input('Escolha a partir do indece: '))
prod6 = int(input('Escolha a partir do indece: '))
meu_carrinho += (lista_prod[prod1],lista_prod[prod2],lista_prod[prod3],
                lista_prod[prod4],lista_prod[prod5],lista_prod[prod6])
meu_total +=    (valores[prod1],valores[prod2],valores[prod3],
                valores[prod4],valores[prod5],valores[prod6])
soma =sum(meu_total)             
print('Meus Produtos: ',meu_carrinho)
print('-----*-----'*10)
print('O total em R$',round(soma,2))