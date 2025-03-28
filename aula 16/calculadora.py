import tkinter as tk

root = tk.Tk()

root.title('CALCULADORA')

root.geometry('300x500')

def soma():
    n1 = float(n1_entry1.get()) 
    n2 = float(n2_entry2.get())
    soma = n1 + n2
    resultado.config(text = f'{soma}')

def sub(a, b):
    n1 = float(n1_entry1.get()) 
    n2 = float(n2_entry2.get())
    sub = n1 - n2
    resultado.config(text = f'{sub}')

def div():
    n1 = float(n1_entry1.get()) 
    n2 = float(n2_entry2.get())
    div = n1 / n2
    resultado.config(text = f'{div}')

def mult():
    n1 = float(n1_entry1.get()) 
    n2 = float(n2_entry2.get())
    mult = n1 * n2
    resultado.config(text = f'{mult}')
    
     


n1_entry1 = tk.Entry(root,width=5)
n1_entry1.grid(column=1,row=0, padx=5,pady=50)

n2_entry2 = tk.Entry(root,width=5)
n2_entry2.grid(column=2,row=0, padx=5,pady=50)

btn1 = tk.Button(root,text='+', command=soma)
btn1.grid(column=1,row=3, padx=5,pady=50)

btn2 = tk.Button(root,text='-', command=sub)
btn2.grid(column=2,row=3, padx=5,pady=50)

btn3 = tk.Button(root,text='/', command=div)
btn3.grid(column=3,row=3, padx=5,pady=50)

btn4 = tk.Button(root,text='*', command=mult)
btn4.grid(column=4,row=3, padx=5,pady=50)

resultado = tk.Label(root, text='=')
resultado.grid(column=3, row=5,padx=10)



root.mainloop() 