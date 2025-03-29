import sqlite3
import tkinter as tk
from tkinter import messagebox


# Função para criar o banco de dados e a tabela
def create_db():
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pessoas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


# Função para salvar o nome no banco de dados
def salvar():
    nome = entry_nome.get()
    
    if nome:  # Verifica se o nome não está vazio
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pessoas (nome) VALUES (?)", (nome,))  # Corrigido para tupla
        conn.commit()
        conn.close()
        messagebox.showinfo('CONFIRMADO', 'EFETUADO COM SUCESSO') 
        listar_nomes()  # Atualiza a lista com o nome salvo
        limpar_campo()  # Limpa o campo de entrada
    else:
        messagebox.showerror('ERRO', 'Algo não funciona. O nome está vazio!')


# Função para listar todos os nomes do banco de dados
def listar_nomes():
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pessoas")
    registros = cursor.fetchall()  # Corrigido para registros
    conn.close()

    # Limpa a lista antes de inserir os novos itens
    listbox.delete(0, tk.END)
    for registro in registros:
        listbox.insert(tk.END, f"ID: {registro[0]}, Nome: {registro[1]}")


# Função para limpar o campo de entrada
def limpar_campo():
    entry_nome.delete(0, tk.END)


# Inicialização da interface gráfica
root = tk.Tk()  # Correção aqui: root = tk.Tk()
root.title('Cadastro de Pessoas')

# Label e Entry para o nome
tk.Label(root, text='Nome: ').grid(row=0, column=0, padx=10, pady=10)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

# Botão para salvar o nome
btn_salvar = tk.Button(root, text='Salvar', command=salvar)  # Correção aqui: Button e command
btn_salvar.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Lista para exibir os nomes cadastrados
listbox = tk.Listbox(root, height=10, width=50)  # Criação de uma listbox para exibir os registros
listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Chamada para criar o banco de dados e tabela na inicialização
create_db()

# Chama a função para listar os nomes quando iniciar
listar_nomes()

# Executa a interface gráfica
root.mainloop()
