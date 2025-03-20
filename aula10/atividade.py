# Sistema de notas de alunos

# - Acesso a conta com condicionais
# - 3 chances de acessar o sistema
# - Após errar 3x, mensagem que diga que a conta foi bloqueada
# - Inserir notas
# - Fazer a média

dados = {'nome': [], 'email': [], 'senha': []}

# Cadastro de usuário
print('Entre no sistema e cadastre nome, email e senha:')
nome = input('Cadastre Nome: ')
email = input('Cadastre Email: ')
senha = input('Cadastre Senha: ')
dados['nome'].append(nome)
dados['email'].append(email)
dados['senha'].append(senha)
print(dados)
print()

# Número de chances para tentar logar
chances = 3

# Loop para o login e entrada de notas
while chances > 0:
    email_usuario = input('Digite o email: ')
    senha_usuario = input('Digite a senha: ')

    # Verifica se o email e a senha estão no mesmo índice
    if email_usuario in dados['email']:
        index_usuario = dados['email'].index(email_usuario)  # Encontrando o índice do usuário
        if senha_usuario == dados['senha'][index_usuario]:  # Verificando se a senha corresponde ao email
            print('\nACESSO PERMITIDO')
            print('Insira suas Notas aqui')

            # Coleta as notas
            try:
                nota1 = float(input('Insira sua primeira nota: '))
                nota2 = float(input('Insira sua segunda nota: '))
                nota3 = float(input('Insira sua terceira nota: '))
            except ValueError:
                print('Por favor, insira apenas números válidos para as notas.')
                continue

            # Calcula a média
            media = round((nota1 + nota2 + nota3) / 3, 2)
            print(f'\nAs suas notas foram: Primeira nota: {nota1}, Segunda nota: {nota2}, Terceira nota: {nota3}')
            print(f'A sua média foi: {media}')

            # Verifica a situação do aluno
            if media >= 9:
                print('APROVADO COM LOUVOR')
            elif media >= 7:  # Correção da lógica
                print('APROVADO')
            elif media >= 4:  # Mantive sua lógica sem o "and media < 7"
                print('RECUPERAÇÃO')
            else:
                print('REPROVADO')

            input('Para sair, digite Enter')
            break
        else:
            chances -= 1
            print('Senha incorreta. Você ainda tem', chances, 'tentativas.')
            if chances == 0:
                print('Acesso negado. Dados incorretos!')
                print('Usuário bloqueado.')
                input('Para sair, digite Enter')
    else:
        chances -= 1
        print('Email incorreto. Você ainda tem', chances, 'tentativas.')
        if chances == 0:
            print('Acesso negado. Dados incorretos!')
            print('Usuário bloqueado.')
            input('Para sair, digite Enter')






