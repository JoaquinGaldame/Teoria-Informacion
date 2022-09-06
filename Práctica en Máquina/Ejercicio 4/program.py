from ast import If
from cgitb import text
from faulthandler import disable
from genericpath import exists
from msilib.schema import Font
from multiprocessing.sharedctypes import Value
from tkinter import *
import math
from tkinter import ttk
from tkinter import font


#Definicion de funciones
def MostrarResultado(IM, HA, PBj):
    resultadoProb = Label(root, text=" Probabilidad Independientes de Salida: {}".format(PBj))
    resultadoProb.pack(side=TOP)
    resultadoProb.config(font="Consolas")
    resEntropiaEmisor = Label(root, text=" Entropía del Emisor: {}".format(HA))
    resEntropiaEmisor.pack(side=TOP)
    resEntropiaEmisor.config(font="Consolas")
    resInfoMutua = Label(root, text=" Informacion Mutua: {}".format(IM))
    resInfoMutua.pack(side=TOP)
    resInfoMutua.config(font="Consolas")

def CalcularInformacionMutua(R, HA, PBj, HAb):
    res = 0
    for i in range(R):
        res += PBj[i] * HAb[i]
    HAB = res
    return (HA - HAB)

def CondicionalesFuente(R):
    count = 0
    res = 0
    for i in range(R):
        for j in range(R):
            res += (Pab[count] * math.log((1/Pab[count]),2))
            count += 1
        HAb.append(float(round(res,ndigits=5)))
        res = 0

def CalcularCondicionalesHaciaAtras(R):
    res= 0
    count = 0
    for i in range(R):
        for j in range(R):
          res += ((P[j] * A[count]) / PBj[i])
          count += 1
          Pab.append((float(round(res,ndigits=2))))
          res = 0 

def calcularEntropiaEntrada(R):
    res = 0
    for i in range(R):
        res += P[i] * math.log((1/P[i]),2)
    return res

def calcularProbabilidad(R):
    count = 0
    resultado = 0
    for i in range(R):
        for j in range(R):
            resultado += (P[j] * A[count])
            count +=1
        PBj.append(round(resultado,ndigits=3))
        resultado = 0

def agregarValores():
    R= opcion.get()
    if R == 2: #4 valores y 2 probabilidades
        A.append(float(entry1.get()))
        A.append(float(entry5.get()))
        A.append(float(entry2.get()))
        A.append(float(entry6.get()))
        P.append(float(entryP1.get()))
        P.append(float(entryP2.get()))
        R = 2
    if R == 3:
        A.append(float(entry1.get()))
        A.append(float(entry5.get()))
        A.append(float(entry9.get()))
        A.append(float(entry2.get()))
        A.append(float(entry6.get()))
        A.append(float(entry10.get()))
        A.append(float(entry3.get()))
        A.append(float(entry7.get()))
        A.append(float(entry11.get()))
        P.append(float(entryP1.get()))
        P.append(float(entryP2.get()))
        P.append(float(entryP3.get()))
        R = 3
    if R == 4:
        A.append(float(entry1.get()))
        A.append(float(entry5.get()))
        A.append(float(entry9.get()))
        A.append(float(entry13.get()))
        A.append(float(entry2.get()))
        A.append(float(entry6.get()))
        A.append(float(entry10.get()))
        A.append(float(entry14.get()))
        A.append(float(entry3.get()))
        A.append(float(entry7.get()))
        A.append(float(entry11.get()))
        A.append(float(entry15.get()))
        A.append(float(entry4.get()))
        A.append(float(entry8.get()))
        A.append(float(entry12.get()))
        A.append(float(entry16.get()))
        P.append(float(entryP1.get()))
        P.append(float(entryP2.get()))
        P.append(float(entryP3.get()))
        P.append(float(entryP4.get()))
        R = 4
    calcularProbabilidad(R)
    HA = calcularEntropiaEntrada(R)
    CalcularCondicionalesHaciaAtras(R)
    CondicionalesFuente(R)
    IM = CalcularInformacionMutua(R, HA, PBj, HAb)
    MostrarResultado(IM,  HA, PBj)
    opcion.set(None)

def mostrar():
    R = opcion.get()
    if R == 2:
        entry1.config(state="normal")
        entry2.config(state="normal")
        entry5.config(state="normal")
        entry6.config(state="normal")
        entryP1.config(state="normal")
        entryP2.config(state="normal")
    elif R == 3:
        entry1.config(state="normal")
        entry2.config(state="normal")
        entry3.config(state="normal")
        entry5.config(state="normal")
        entry6.config(state="normal")
        entry7.config(state="normal")
        entry9.config(state="normal")
        entry10.config(state="normal")
        entry11.config(state="normal")
        entryP1.config(state="normal")
        entryP2.config(state="normal")
        entryP3.config(state="normal")
    elif R == 4:
        entry1.config(state="normal")
        entry2.config(state="normal")
        entry3.config(state="normal")
        entry4.config(state="normal")
        entry5.config(state="normal")
        entry6.config(state="normal")
        entry7.config(state="normal")
        entry8.config(state="normal")
        entry9.config(state="normal")
        entry10.config(state="normal")
        entry11.config(state="normal")
        entry12.config(state="normal")
        entry13.config(state="normal")
        entry14.config(state="normal")
        entry15.config(state="normal")
        entry16.config(state="normal")
        entryP1.config(state="normal")
        entryP2.config(state="normal")
        entryP3.config(state="normal")
        entryP4.config(state="normal")
    else:
        mensaje = Label(root, text="Debe seleccionar un valor").pack()

#Configuración de la Interfaz
root=Tk()
menubar = Menu(root)
root.config(menu=menubar)
root.title("Ejercicio 3")
root.resizable(False,False)
root.geometry('720x540')
root.config(bg = "lightblue")


#Primer Marco de la interfaz
frame = Frame(root)
frame.pack(side=TOP)
frame.config(width=380, height=220)
texto= Label(frame, text=" Seleccionar el valor de R ")
texto.pack()
texto.config(font="Consolas")
################ TABLA - MATRIZ ########################
frame2 = Frame(root)
frame2.pack(side=BOTTOM)
frame2.config(width=380, height=220)
texto2= Label(root, text=" Ingresar probabilidades ")
texto2.pack(side=BOTTOM)
texto2.config(font="Consolas")
label = Label(frame2, text ="A1")
label.grid(row=1, column=1, padx=5, pady=5)
entryP1 = Entry(frame2)
entryP1.grid(row=1, column=0, padx=5, pady=5)
entryP1.config(justify=CENTER, state="disabled")
label2 = Label(frame2, text ="A2")
label2.grid(row=2, column=1, padx=5, pady=5)
entryP2 = Entry(frame2)
entryP2.grid(row=2, column=0, padx=5, pady=5)
entryP2.config(justify=CENTER, state="disabled")
label3 = Label(frame2, text ="A3")
label3.grid(row=3, column=1, padx=5, pady=5)
entryP3 = Entry(frame2)
entryP3.grid(row=3, column=0, padx=5, pady=5)
entryP3.config(justify=CENTER, state="disabled")
label4 = Label(frame2, text ="A4")
label4.grid(row=4, column=1, padx=5, pady=5)
entryP4 = Entry(frame2)
entryP4.grid(row=4, column=0, padx=5, pady=5)
entryP4.config(justify=CENTER, state="disabled")
label5 = Label(frame2, text ="B1") # COLUMNA 1
label5.grid(row=0, column=2, padx=5, pady=5)
entry1 = Entry(frame2)
entry1.grid(row=1, column=2, padx=5, pady=5)
entry1.config(justify=CENTER, state="disabled")
entry2 = Entry(frame2)
entry2.grid(row=2, column=2, padx=5, pady=5)
entry2.config(justify=CENTER, state="disabled")
entry3 = Entry(frame2)
entry3.grid(row=3, column=2, padx=5, pady=5)
entry3.config(justify=CENTER, state="disabled")
entry4 = Entry(frame2)
entry4.grid(row=4, column=2, padx=5, pady=5)
entry4.config(justify=CENTER, state="disabled")
label6 = Label(frame2, text ="B2") # COLUMNA 2
label6.grid(row=0, column=3, padx=5, pady=5)
entry5 = Entry(frame2)
entry5.grid(row=1, column=3, padx=5, pady=5)
entry5.config(justify=CENTER, state="disabled")
entry6 = Entry(frame2)
entry6.grid(row=2, column=3, padx=5, pady=5)
entry6.config(justify=CENTER, state="disabled")
entry7 = Entry(frame2)
entry7.grid(row=3, column=3, padx=5, pady=5)
entry7.config(justify=CENTER, state="disabled")
entry8 = Entry(frame2)
entry8.grid(row=4, column=3, padx=5, pady=5)
entry8.config(justify=CENTER, state="disabled")
label7 = Label(frame2, text ="B3") # COLUMNA 3
label7.grid(row=0, column=4, padx=5, pady=5)
entry9 = Entry(frame2)
entry9.grid(row=1, column=4, padx=5, pady=5)
entry9.config(justify=CENTER, state="disabled")
entry10 = Entry(frame2)
entry10.grid(row=2, column=4, padx=5, pady=5)
entry10.config(justify=CENTER, state="disabled")
entry11 = Entry(frame2)
entry11.grid(row=3, column=4, padx=5, pady=5)
entry11.config(justify=CENTER, state="disabled")
entry12 = Entry(frame2)
entry12.grid(row=4, column=4, padx=5, pady=5)
entry12.config(justify=CENTER, state="disabled")
label8 = Label(frame2, text ="B4") # COLUMNA 4
label8.grid(row=0, column=5, padx=5, pady=5)
entry13 = Entry(frame2)
entry13.grid(row=1, column=5, padx=5, pady=5)
entry13.config(justify=CENTER, state="disabled")
entry14 = Entry(frame2)
entry14.grid(row=2, column=5, padx=5, pady=5)
entry14.config(justify=CENTER, state="disabled")
entry15 = Entry(frame2)
entry15.grid(row=3, column=5, padx=5, pady=5)
entry15.config(justify=CENTER, state="disabled")
entry16 = Entry(frame2)
entry16.grid(row=4, column=5, padx=5, pady=5)
entry16.config(justify=CENTER, state="disabled")

#################  FIN MATRIZ ##########################
A = [] # Probabilidades dadas 
P = [] # Probabilidades Independientes de la entrada
PBj = [] # Probabilidades Independientes de la Salida
Pab = [] # Prababilidades Condicionales Hacia Atras
HA = 0  # Entropia del Emisor
HAb = [] # Condicionales de la fuente
HAB = 0 # Condicional de Entropia
IM = 0
opcion = IntVar()
Radiobutton(frame, text=" R = 2 ", variable=opcion, value=2,).pack()
Radiobutton(frame, text=" R = 3 ", variable=opcion, value=3).pack()
Radiobutton(frame, text=" R = 4 ", variable=opcion, value=4).pack()
button = Button(frame, text="Aceptar", command=mostrar).pack()
button2 = Button(root, text="Calcular", command=agregarValores)
button2.pack(side=BOTTOM, anchor="center")
#Finalmente bucle
root.mainloop()