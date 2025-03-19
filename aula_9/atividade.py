# Crie um sistema de notas, com as seguintes operações:
# ***Utilize While ou for*** 
# # Sistema de notas de alunos

# - Acesso a conta com condicionais

# - 3 chances de acessar o sistema

# - Após errar 3 x mensagem que diga que a conta bloqueada 
# - Inserir notas 
# - Fazer a média

dados = {'nome': [], 'email':[],'senha':[]}


print('Entre no sistema cadastre nome ,email e senha:')
nome = input('Cadastre Nome: ')
email = input('Cadastre Email: ')
senha = input('Cadastre senha: ')
dados['nome'].append(nome)
dados['email'].append(email)
dados['senha'].append(senha)
print(dados)
print()
dados_usuario = dados
chances = 3
while chances > 0 :
    email_usuario = input('Digite o email ')
    senha_usuario = input('Digite a senha ')
    if email_usuario in dados['email'] and senha_usuario in dados['senha']:
        print('ACESSO PERMITIDO')
        nota1 = float(input('Inserir sua  primeira nota aqui: '))
        nota2 = float(input('Inserir sua  segunda nota aqui: '))
        nota3 = float(input('Inserir sua  terceira nota aqui: '))
        media = round((nota1+ nota2 + nota3)/3,2)
        print('As suas notas foram Primeira nota ',nota1,' Segunda nota ',nota2,' e Terceira nota',nota3)
        print('A sua media foi ',media)
        
        if media >= 9:
            print('APROVADO COM LOUVOR')
        elif media >= 7 or media < 9:
            print('APROVADO')
        elif media >4 or media < 7:
            print('RECUPERAÇÃO')
        elif media <=4:
            print('REPROVADO')
            
        input('Para sair digite Enter')
        break
    else:
        chances -= 1
        print('Você errou a email ou a senha')
        print('tente novamente')
        if chances == 0:
            print('Acesso negado dados incorretos! ') 
            print('Usuário Bloqueado') 
            input('Para sair digite Enter')
        
        





