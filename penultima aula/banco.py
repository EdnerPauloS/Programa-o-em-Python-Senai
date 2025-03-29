import sqlite3
conexao = sqlite3.connect('meu_banco_de_dados.db')

cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS pessoas (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome TEXT NOT NULL ,
    idade INTEGER NOT NULL,
    cidade TEXT NOT NULL
)
''')

nome = input('Digite um nome: ')
idade = input('Digite sua idade: ')
cidade = input('Cidade:   ')

cursor.execute('''
    INSERT INTO pessoas (nome, idade, cidade) VALUES (?,?,?)
''',(nome,idade,cidade))

conexao.commit()

cursor.execute('SELECT * FROM pessoas')

pessoas =  cursor.fetchall()

for pessoa in pessoas:
    print(f'''ID:{pessoa[0]},Nome:{pessoa[1]},Idade: {pessoa[2]}. Cidade:{pessoa[3]}''')
    
conexao.close()



# conexao.commit()

# # Excluir (dropar) a tabela 'pessoas'
# cursor.execute('DROP TABLE IF EXISTS pessoas')

# # Consultar os dados (agora não existe mais a tabela)
# # Isso irá gerar erro porque a tabela foi excluída acima.
# try:
#     cursor.execute('SELECT * FROM pessoas')
#     pessoas = cursor.fetchall()
#     for pessoa in pessoas:
#         print(f'ID: {pessoa[0]}, Nome: {pessoa[1]}, Idade: {pessoa[2]}, Cidade: {pessoa[3]}')
# except sqlite3.OperationalError as e:
#     print(f'Erro: {e}')  # Aqui a tabela foi excluída, então o erro esperado será informado.

# # Fechar a conexão
# conexao.close()