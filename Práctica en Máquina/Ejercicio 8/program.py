from ctypes import sizeof
from readline import insert_text
from tkinter import *
import math
from turtle import bgcolor 

def validar_cuit(cuit):
    # validaciones minimas
    if len(cuit) != 13 or cuit[2] != "-" or cuit[11] != "-":
        return 0

    base = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]

    cuit = cuit.replace("-", "") # remuevo las barras

    # calculo el digito verificador:
    aux = 0
    for i in range(10):
        aux += int(cuit[i]) * base[i]

    aux = 11 - (aux - (int(aux / 11) * 11))

    if aux == 11:
        aux = 0
    if aux == 10:
        aux = 9
    if aux == int(cuit[10]):
        return 1
    else: return 2

def clik():
    cuit = entry.get()
    numero = validar_cuit(cuit)
    if numero == 0:
        label3 = Label(root, text="Ingrese correctamente Número de CUIL")
        label3.pack(side=TOP)
        label3.config(font="Consolas", bg="honeydew2")
    elif numero == 1:
        label4 = Label(root, text="Número de CUIL válido")
        label4.pack(side=TOP)
        label4.config(font="Consolas", bg="honeydew2")
    elif numero == 2:
        label5 = Label(root, text="Número de CUIL inválido")
        label5.pack(side=TOP)
        label5.config(font="Consolas", bg="honeydew2")
    entry.delete(0,len(entry.get()))
        


root=Tk()
menubar = Menu(root)
root.config(menu=menubar)
root.title("Ejercicio 8")
root.resizable(False,False)
root.geometry('480x320')
root.config(bg = "honeydew2")
filemenu = Menu(menubar, tearoff=0)
editmenu = Menu(menubar, tearoff=0)
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Archivo", menu = filemenu)
menubar.add_cascade(label = "Editar", menu = editmenu)
menubar.add_cascade(label = "Ayuda", menu = helpmenu)

cuit = StringVar
label = Label(root, text="INGRESAR CUIL/CUIT")
label.pack(side=TOP)
label.config(font="Consolas", bg="honeydew2")
label2 = Label(root, text="con guiones")
label2.pack(side=TOP)
label2.config(font="Consolas", bg="honeydew2")
entry = Entry(root)
entry.pack(side=TOP)
entry.config(justify=CENTER, font="Consolas")
button = Button(root, text="Validar", command=clik)
button.pack(side=TOP)
button.config(font="Consolas", justify=CENTER)
root.mainloop()

