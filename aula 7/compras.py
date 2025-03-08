print('Mercado')

produtos =  ['Livros', 'Tablets','Fones de Ouvido', 'Celulares']
valores  =  [50.0,250.00,15.00,2000.00]
carrinho = []
meu_valores = []

produto1 =  int(input('''
0 - Livros
1 - Tablets 
2 - Fones de Ouvido
3 - Celulares
>> '''))

produto2 = int(input('''
0 - Livros
1 - Tablets 
2 - Fones de Ouvido
3 - Celulares
>> '''))


carrinho = [produtos[produto1], produtos[produto2]]
meu_valores = [valores[produto1], valores[produto2]]
SOMA =  sum(meu_valores)

print(f'''
.................................
CUPOM

1 - {produtos[produto1]} R$ {valores[produto1]:.2f}
2 - {produtos[produto2]} R$ {valores[produto2]:.2f}

.................................
R$ {SOMA:.2f}

OBRIGADO POR COMPRA COM A GENTE

''')
