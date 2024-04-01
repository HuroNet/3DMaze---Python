from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk,Image, ImageChops, ImageEnhance, ImageOps #llama a las imagenes
import math # librerias matematica

ventana = Tk()
ventana.title("Datos del Jugador")
#ventana.geometry("630x450")
ventana.geometry("280x220")


L1=Label(ventana,text="Numero de Jugador: ")  #Label -> la parte escrita 
L1.place(x=8,y=8)
E1=Entry(ventana)                       #Entry -> la parte de los cuadros
E1.place(x=135,y=8)

L2=Label(ventana,text="Nombre del Jugador: ")  #Label -> la parte escrita 
L2.place(x=8,y=50)
E2=Entry(ventana)                       #Entry -> la parte de los cuadros
E2.place(x=135,y=50)

L3=Label(ventana,text="Edad del Jugador: ")  #Label -> la parte escrita 
L3.place(x=8,y=90)
E3=Entry(ventana)                       #Entry -> la parte de los cuadros
E3.place(x=135,y=90)
ventana['bg'] = '#49A'


def datosIngresados():
    numeroJ = E1.get()
    nombreJ = (E2.get())
    edadJ = int(E3.get())

    print(numeroJ,nombreJ,edadJ)
    

def clearText():
    E1.delete(0,END)
    E2.delete(0,END)
    E3.delete(0,END)
    

B1=Button(ventana, text="Aceptar" , command= datosIngresados)
B1.place(x=50,y=150)
#print(type(B1))



B2=Button(ventana, text="Limpiar" ,  command=clearText)
B2.place(x=155 ,y=150)

ventana.mainloop()

