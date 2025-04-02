import sqlite3
import tkinter as tk
from tkinter import messagebox

# Função para criar o banco de dados e a tabela
def create_db():
    conn = sqlite3.connect('leads.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL,
            interesse TEXT NOT NULL,
            status TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Função para salvar um novo lead
def salvar():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    interesse = entry_interesse.get()
    status = var_status.get()  # Pegando o status selecionado pelos RadioButtons

    if nome and email and telefone and interesse and status:
        conn = sqlite3.connect('leads.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO leads (nome, email, telefone, interesse, status) 
            VALUES (?, ?, ?, ?, ?)
        ''', (nome, email, telefone, interesse, status))
        conn.commit()
        conn.close()
        messagebox.showinfo('CONFIRMADO', 'Lead cadastrado com sucesso!')
        listar_leads()  # Atualiza a lista de leads
        limpar_campos()  # Limpa os campos
    else:
        messagebox.showerror('ERRO', 'Preencha todos os campos!')

# Função para listar os leads
def listar_leads():
    conn = sqlite3.connect('leads.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM leads")
    leads = cursor.fetchall()
    conn.close()

    listbox_leads.delete(0, tk.END)
    for lead in leads:
        listbox_leads.insert(tk.END, f"ID: {lead[0]}, Nome: {lead[1]}, Status: {lead[5]}")

# Função para editar o lead selecionado
def editar():
    selecionado = listbox_leads.curselection()
    if selecionado:
        indice = selecionado[0]
        lead_id = listbox_leads.get(indice).split(',')[0].split(':')[1].strip()

        conn = sqlite3.connect('leads.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM leads WHERE id = ?", (lead_id,))
        lead = cursor.fetchone()
        conn.close()

        entry_nome.delete(0, tk.END)
        entry_nome.insert(0, lead[1])
        entry_email.delete(0, tk.END)
        entry_email.insert(0, lead[2])
        entry_telefone.delete(0, tk.END)
        entry_telefone.insert(0, lead[3])
        entry_interesse.delete(0, tk.END)
        entry_interesse.insert(0, lead[4])

        # Seleciona o status correspondente
        if lead[5] == "Em andamento":
            var_status.set("Em andamento")
        elif lead[5] == "Convertido":
            var_status.set("Convertido")
        else:
            var_status.set("Perdido")

        btn_salvar.config(state=tk.DISABLED)  # Desabilita o botão salvar
        btn_atualizar.config(state=tk.NORMAL)  # Habilita o botão de atualização

        # Atualizar o lead no banco de dados
        def atualizar():
            nome = entry_nome.get()
            email = entry_email.get()
            telefone = entry_telefone.get()
            interesse = entry_interesse.get()
            status = var_status.get()

            conn = sqlite3.connect('leads.db')
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE leads SET nome = ?, email = ?, telefone = ?, interesse = ?, status = ?
                WHERE id = ?
            ''', (nome, email, telefone, interesse, status, lead_id))
            conn.commit()
            conn.close()

            messagebox.showinfo('ATUALIZADO', 'Lead atualizado com sucesso!')
            listar_leads()
            limpar_campos()
            btn_salvar.config(state=tk.NORMAL)
            btn_atualizar.config(state=tk.DISABLED)

        btn_atualizar.config(command=atualizar)

    else:
        messagebox.showerror('ERRO', 'Selecione um lead para editar.')

# Função para deletar o lead selecionado
def deletar():
    selecionado = listbox_leads.curselection()
    if selecionado:
        indice = selecionado[0]
        lead_id = listbox_leads.get(indice).split(',')[0].split(':')[1].strip()

        conn = sqlite3.connect('leads.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM leads WHERE id = ?", (lead_id,))
        conn.commit()
        conn.close()

        messagebox.showinfo('DELETADO', 'Lead deletado com sucesso!')
        listar_leads()
    else:
        messagebox.showerror('ERRO', 'Selecione um lead para deletar.')

# Função para limpar os campos de entrada
def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    entry_interesse.delete(0, tk.END)
    var_status.set('Em andamento')  # Reseta para a opção padrão

# Configuração da interface gráfica
root = tk.Tk()
root.title('Cadastro de Leads')

# Label e Entry para o nome
tk.Label(root, text='Nome: ').grid(row=0, column=0, padx=10, pady=10)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

# Label e Entry para o e-mail
tk.Label(root, text='E-mail: ').grid(row=1, column=0, padx=10, pady=10)
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1, padx=10, pady=10)

# Label e Entry para o telefone
tk.Label(root, text='Telefone: ').grid(row=2, column=0, padx=10, pady=10)
entry_telefone = tk.Entry(root)
entry_telefone.grid(row=2, column=1, padx=10, pady=10)

# Label e Entry para o interesse
tk.Label(root, text='Interesse: ').grid(row=3, column=0, padx=10, pady=10)
entry_interesse = tk.Entry(root)
entry_interesse.grid(row=3, column=1, padx=10, pady=10)

# Radiobuttons para status (substituindo o Combobox)
tk.Label(root, text='Status: ').grid(row=4, column=0, padx=10, pady=10)
var_status = tk.StringVar(value="Em andamento")  # Valor inicial
tk.Radiobutton(root, text="Em andamento", variable=var_status, value="Em andamento").grid(row=4, column=1, padx=5, pady=5, sticky="w")
tk.Radiobutton(root, text="Convertido", variable=var_status, value="Convertido").grid(row=5, column=1, padx=5, pady=5, sticky="w")
tk.Radiobutton(root, text="Perdido", variable=var_status, value="Perdido").grid(row=6, column=1, padx=5, pady=5, sticky="w")

# Botão para salvar o lead
btn_salvar = tk.Button(root, text='Salvar', command=salvar)
btn_salvar.grid(row=7, column=0, padx=10, pady=10)

# Botão para editar o lead
btn_atualizar = tk.Button(root, text='Atualizar', state=tk.DISABLED)
btn_atualizar.grid(row=7, column=1, padx=10, pady=10)

# Botão para deletar o lead
btn_deletar = tk.Button(root, text='Deletar', command=deletar)
btn_deletar.grid(row=7, column=2, padx=10, pady=10)

# Listbox para exibir os leads cadastrados
listbox_leads = tk.Listbox(root, height=10, width=80)
listbox_leads.grid(row=8, column=0, columnspan=3, padx=10, pady=10)

# Função para criar o banco de dados
create_db()

# Função para listar os leads ao iniciar
listar_leads()

# Executa a interface gráfica
root.mainloop()
