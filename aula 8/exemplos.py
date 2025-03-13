pessoa = {
    'carlos':{
    'nome' :'Carlos',
    'idade': 30,
    'graduacao': 'ADS',
    'senha': 1234,
    'login':'@carlos'
},
    'Fernanda':{   
    'nome':'Fernanda',
    'idade':30,
    'graduação':'ADS',
    'senha':4321,
    'login':'@fernanda',
    'Brasileiro':True
}
}

login = input('Digite seu login: ')
senha = int(input('Digite sua senha: '))

if login == pessoa['login'] and senha == pessoa['senha']:
    print('ACESSO AUTORIZADO')
else:
    print('ACESSO NEGADO')

