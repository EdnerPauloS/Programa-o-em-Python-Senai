# dict

dicionario = {
'key1':'valor1',
'key2':'valor2',
'key3':'valor3',
True: 'valor4',
10 : 'valor5',
20.6 : 'valor6',
}
print(dicionario)

pessoa_ ={
    'nome':'Caio',
    'idade': 25,
    'curso':['c','c#','php','js', 'python','mojo'], 
    'endereco':'rua 25',
    'experiencia':{
    'a':'empresa1',
    'b':'empresa2',
    'teste':{'a':100,'b':200,'c':300}
    },
    'documentos':('rg- 123456', 'cpf - 7894561230')
}
print(pessoa_)
print(pessoa_['curso'][4])
print(pessoa_['experiencia']['b'])
print(pessoa_['experiencia']['teste'])
