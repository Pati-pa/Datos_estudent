#---------------------------------
# Desktop app No. 2- Temperatura
#---------------------------------

# se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox, ttk

#-------------------------
# funciones de la app
#-------------------------

# abrir toplevel centigrados
def abrir_toplevel_centigrados():
    global toplevel_centigrados
    toplevel_centigrados = Toplevel()
    toplevel_centigrados.title("Promedio")
    toplevel_centigrados.resizable(False, False)
    toplevel_centigrados.geometry("400x250")
    toplevel_centigrados.config(bg="white")

    # logo de la app
    lb_logo2 = Label(toplevel_centigrados, image=logo, bg="white")
    lb_logo2.place(x=10,y=10)

    # etiqueta para valor en centigrados
    lb_note = Label(toplevel_centigrados, text = "°C = ")
    lb_note.config(bg="white", fg="blue", font=("Helvetica", 18))
    lb_note.place(x=150, y=60)
    lb_note2 = Label(toplevel_centigrados, text = "Nota = ")
    lb_note2.config(bg="white", fg="cyan", font=('Gabriola', 18))
    lb_note2.place(x=120, y=90)
    lb_note3= Label(toplevel_centigrados, text = "Nota = ")
    lb_note3.config(bg="white", fg="cyan", font=('Gabriola', 18))
    lb_note3.place(x=120, y=130)

    # caja de texto para valor en centigrados
    entry_note = Entry(toplevel_centigrados, textvariable=note)
    entry_note.config(bg="white", fg="blue", font=("Times New Roman", 18), width=6)
    entry_note.focus_set()
    entry_note.place(x=210,y=60)
    entry_note2 = Entry(toplevel_centigrados, textvariable=note2)
    entry_note2.config(bg="white", fg="blue", font=("Times New Roman", 18), width=6)
    entry_note2.focus_set()
    entry_note2.place(x=210,y=100)
    entry_note3 = Entry(toplevel_centigrados, textvariable=note3)
    entry_note3.config(bg="white", fg="blue", font=("Times New Roman", 18), width=6)
    entry_note3.focus_set()
    entry_note3.place(x=210,y=140)

   # boton para convertir
    bt_aceptar = Button(toplevel_centigrados,text="Aceptar", command=aceptar)
    bt_aceptar.place(x=100, y=200, width=100, height=30)

# aceptar
def aceptar():
    global cent
    cent = int(note.get())
    toplevel_centigrados.destroy()

# convertir
def convertir():
    messagebox.showinfo("Temperatura 1.0", "Conversión realizada")
    cent = int(note.get())
    cent1 = int(note2.get())
    cent2 = int(note3.get())
    suma = cent + cent1 + cent2
    temp = cmb_kf.get()
    if temp == "Kelvin":
        k = suma/3
        t_resultados.insert(INSERT, f"\n{int(suma)} °C equivalen a {k} °K")
    elif temp == "Fahrenheit":
        f = cent*9/5 + 32
        t_resultados.insert(INSERT, f"\n{int(suma)} °C equivalen a {f} °F")
    else:
        t_resultados.insert(INSERT, "Debe seleccionar una opción")
    
# borrar
def borrar():
    messagebox.showinfo("Temperatura 1.0", "Los datos serán borrados")
    c.set("")
    t_resultados.delete("1.0","end")

# salir
def salir():
    messagebox.showinfo("Temperatura 1.0", "La app se va a cerrar")
    ventana_principal.destroy()

#-----------------------------
# ventana principal de la app
#-----------------------------

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Temperatura 1.0")

# tamaño de la ventana
ventana_principal.geometry("500x500")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="blue")

#--------------------------------
# variables globales
#--------------------------------
note = StringVar()
note2 = StringVar()
note3 = StringVar()
kf = ["Kelvin", "Fahrenheit"]
kf_selected = StringVar()
global logo

#--------------------------------
# frame entrada datos
#--------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=480, height=180)
frame_entrada.place(x=10, y=10)

# logo de la app
logo = PhotoImage(file="img/doctor.png")
lb_logo = Label(frame_entrada, image=logo, bg="white")
lb_logo.place(x=70,y=40)

# titulo de la app
titulo = Label(frame_entrada, text="Termperatura 1.0")
titulo.config(bg = "white",fg="blue", font=("Helvetica", 20))
titulo.place(x=240,y=10)

# boton para abrir Toplevel para ingresar °C
bt_centigrados = Button(frame_entrada, text="Ingresar °C", command=abrir_toplevel_centigrados)
bt_centigrados.place(x=240, y=60)
# lista para kelvin y fahrenheit
cmb_kf = ttk.Combobox(frame_entrada, textvariable=kf_selected, values=kf, font=("Helvetica", 12))
cmb_kf.place(x=240, y=110)



#--------------------------------
# frame operaciones
#--------------------------------
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white", width=480, height=100)
frame_operaciones.place(x=10, y=200)

# boton para convertir
bt_convertir = Button(frame_operaciones,text="Convertir", command=convertir)
bt_convertir.place(x=45, y=35, width=100, height=30)

# boton para borrar
bt_borrar = Button(frame_operaciones, text="Borrar", command=borrar)
bt_borrar.place(x=190, y=35, width=100, height=30)

# boton para salir
bt_salir = Button(frame_operaciones,text="Salir", command=salir)
bt_salir.place(x=335, y=35, width=100, height=30)

#--------------------------------
# frame resultados
#--------------------------------
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="white", width=480, height=180)
frame_resultados.place(x=10, y=310)

# area de texto para los resultados
t_resultados = Text(frame_resultados)
t_resultados.config(bg="black", fg="green yellow", font=("Courier", 18))
t_resultados.place(x=10,y=10,width=460,height=160)

# run
# se ejecuta el metodo mainloop() de la clase Tk() a través de la instancia ventana_principal. Este metodo despliega la ventana en pantalla y queda a la espera de lo que el usuario haga (click en un boton, escribir, etc).  Cada acción del usuario se conoce como un evento.  El método mainloop() es un bucle infinito.
ventana_principal.mainloop()



elif temp == "Promedio necesario": 
        f = suma/3 == promedio_dese
        t_resultados.insert(INSERT, (f"\n""El promedio es igual al valor ingresado"))
    elif temp == "Promedio necesario":
        f = suma/3 > promedio_dese
        t_resultados.insert(INSERT, (f"\n""El promedio es mayor al valor ingresado"))




 if promedio == promedio_dese:
            t_resultados.insert(INSERT, "¡Ya has alcanzado el promedio deseado!")
        elif promedio < promedio_dese:
            falta = promedio_dese - promedio
            t_resultados.insert(INSERT, f"Falta {falta} para alcanzar el promedio deseado.")
        else:
            sobra = promedio - promedio_dese
            t_resultados.insert(INSERT, f"Has superado el promedio deseado por {sobra}.")


            from tkinter import messagebox, ttk
import tkinter as tk

def selection_changed(event):
    selection = combo.get()
    messagebox.showinfo(
        title="Nuevo elemento seleccionado",
        message=selection
    )

main_window = tk.Tk()
main_window.config(width=300, height=200)
main_window.title("Combobox")
combo = ttk.Combobox(values=["Python", "C", "C++", "Java"])
combo.bind("<<ComboboxSelected>>", selection_changed)
combo.place(x=50, y=50)
main_window.mainloop()
