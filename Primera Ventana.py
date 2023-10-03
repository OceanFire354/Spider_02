#from tkinter import *
import tkinter as tk
raiz = tk.Tk()
raiz.title("Primera ventana")
raiz.geometry("520x480")
Boton = tk.Button(raiz, text = "Hola, Mundo")
Boton.place (x=50, y=50)
Entrada = tk.Entry()
Entrada.place(x=50, y=160,width=150)
raiz.mainloop()