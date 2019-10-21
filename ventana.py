from tkinter import *

def ventana(titulo,etiqueta):
    window = Tk()
    window.title(titulo)
    window.geometry('300x35')
    window.resizable(width=False, height=False)
    valor = IntVar()
  
    lbl = Label(window, text=etiqueta)
    lbl.grid(column=1, row=1)
    txt = Entry(window, textvariable = valor, width=10).grid(column = 2,row = 1)
    
    def clicked():
        window.destroy()
        print (valor.get())
    
    btn = Button(window, text="Aceptar", command=clicked)
    btn.grid(column=3, row=1)
    
    window.mainloop()
    return valor.get()