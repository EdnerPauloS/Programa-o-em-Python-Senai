import sqlite3

# Conectar ao banco de dados
conexao = sqlite3.connect("tutorial.db")
cursor = conexao.cursor()

# Criar a tabela 'filme' se não existir
cursor.execute("""
    CREATE TABLE IF NOT EXISTS filme (
        titulo TEXT,  -- Título do filme
        ano INTEGER,  -- Ano de lançamento do filme
        pontuacao REAL  -- Pontuação do filme
    )
""")

conexao.commit()

# Inserir dados na tabela 'filme'
cursor.execute("""
    INSERT INTO filme (titulo, ano, pontuacao) VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")

conexao.commit()

# Consultar todas as pontuações dos filmes
resultado = cursor.execute("SELECT pontuacao FROM filme")
print(resultado.fetchall())  # Exibindo as pontuações: [(8.2,), (7.5,)]

# Inserir mais dados usando executemany
dados = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]
cursor.executemany("INSERT INTO filme (titulo, ano, pontuacao) VALUES(?, ?, ?)", dados)
conexao.commit()  # Lembre-se de confirmar a transação após o INSERT

# Mostrar os filmes ordenados pelo ano
for linha in cursor.execute("SELECT ano, titulo FROM filme ORDER BY ano"):
    print(linha)  # Exibindo os filmes ordenados pelo ano
# Saída esperada:
# (1971, 'And Now for Something Completely Different')
# (1975, 'Monty Python and the Holy Grail')
# (1979, "Monty Python's Life of Brian")
# (1982, 'Monty Python Live at the Hollywood Bowl')
# (1983, "Monty Python's The Meaning of Life")

# Fechar a conexão com o banco de dados
conexao.close()

# Reabrir a conexão para uma nova consulta
nova_conexao = sqlite3.connect("tutorial.db")
novo_cursor = nova_conexao.cursor()

# Consultar o filme com a maior pontuação
resultado = novo_cursor.execute("SELECT titulo, ano FROM filme ORDER BY pontuacao DESC")
titulo, ano = resultado.fetchone()
print(f'O filme Monty Python com a maior pontuação é {titulo!r}, lançado em {ano}')
# Saída esperada: O filme Monty Python com a maior pontuação é 'Monty Python and the Holy Grail', lançado em 1975

# Fechar a conexão final
nova_conexao.close()