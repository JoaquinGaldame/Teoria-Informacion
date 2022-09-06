from cProfile import label
from cgitb import reset
from ctypes.wintypes import DOUBLE
from itertools import count
from tkinter import *
import math 
from unittest import result
def MostrarResultado():
    resultadoProb = Label(root, text=" Probabilidad Independientes de Salida: {}".format(PB))
    resultadoProb.pack(side=TOP)
    resultadoProb.config(font="Consolas")
def agregarValor():
    resultado = 0
    count = 0
    for i in range(R):
        for j in range(R):
            resultado += P[j] * A[count]
            count +=1
        PB.append(resultado)
        resultado = 0
    print(PB)

def CalcularInformacionMutua():
    res = 0
    for i in range(R):
        res += PB[i] * HAb[i]
    HAB = res
    print(HAB)
    IAB = HA - HAB
    print(IAB)

def CondicionalesHaciaAtras():
    res= 0
    count = 0
    for i in range(R):
        for j in range(R):
          res += ((P[j] * A[count]) / PB[i])
          count += 1
          Pab.append((float(round(res,ndigits=2))))
          res = 0
    print(Pab)
    CondicionalesFuente()
    CalcularInformacionMutua()
    MostrarResultado()

def CondicionalesFuente():
    count = 0
    res = 0
    for i in range(R):
        for j in range(R):
            res += (Pab[count] * math.log((1/Pab[count]),2))
            count += 1
        HAb.append(float(res))
        res = 0
    print(HAb)


def entropia():
    count = 0
    resultado = 0
    for i in range(R):
        resultado += P[i] * math.log((1/P[i]),2)
        print(resultado)

#Configuración de la raíz
root=Tk()
root.title("Ejercicio 3")
root.resizable(1,1)
root.config(width=380, height=220)

frame = Frame(root)
frame.pack()
frame.config(width=380, height=220)
Pab = []
A = [0.875, 0.125, 0.125, 0.875]
P = [0.2, 0.8]
PB = [0.275, 0.725]
HA = 0.72193
HAb = []
HAB = 0
IAB = 0
R=2
N = R*R
label = Label(frame, text="El valor es: ").pack()
button = Button(frame, text="Agregar", command=CondicionalesHaciaAtras).pack()

#Finalmente bucle
root.mainloop()