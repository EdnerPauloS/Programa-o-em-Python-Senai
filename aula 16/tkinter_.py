import tkinter as tk
#importa a biblioteca

def display():
    print('Isso é um print')

def display2():
    texto = entry1.get()
    text_label2.config(text=f'texto')

janela = tk.Tk()
janela.title('Teste do Tkinter')
#titulo da janela
janela.geometry('500x500')
# tamanho do  janela
text_label = tk.Label(janela, text='ISSO É UM TEXTO')
text_label.pack(pady=10)
# cria um texto dentro da janela
entry1 = tk.Entry(janela)
entry1.pack(pady=10)
#espaço para digitação um input
btn = tk.Button(janela, text='Escreve um texto no terminal',command=display)
btn.pack(pady=10)
# command escreve um texto no prompt
#cria um botão 
btn1 = tk.Button(janela, text='Escreve um Texto na tela',command=display)
btn1.pack(pady=10)

text_label2 = tk.Label(janela, text='Aqui vai aparecer um texto')
text_label.pack(pady=10)

janela.mainloop() 
# coloca a janela em loop