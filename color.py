import tkinter as tk
import tkinter.ttk as ttk
from tkcolorpicker import askcolor

def color():
    root = tk.Tk()
    style = ttk.Style(root)
    style.theme_use('clam')

    color = askcolor(title="Seleccione color")
    root.destroy()
    root.mainloop()
    return color