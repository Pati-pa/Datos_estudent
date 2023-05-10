#------------------
# Ayuda Uis
#------------------

# se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox, ttk
import tkinter as tk

#Funciones de la app
#funcion para el enter

#--------------------------
#Función de convertir
def convertir():
    messagebox.showinfo("Promedio", "Promedio listo")
    cent = int(note.get())
    cent2 = int(note2.get())
    cent3 = int(note3.get())
    promedio_dese = int(promedio_deseado.get())
    suma = cent + cent2 + cent3
    promedio = suma/3
    temp = cmb_kf.get()
    if temp == "Promedio":
        k = promedio
        t_resultados.insert(INSERT, (f"\n"f"Este es tu promedio {k}"))
    elif temp == "Promedio deseado":
        if promedio == promedio_dese:
            t_resultados.insert(INSERT, "¡Ya has alcanzado el promedio deseado!")
        elif promedio < promedio_dese:
            falta = promedio_dese - promedio
            t_resultados.insert(INSERT, f"Falta {falta} para alcanzar el promedio deseado.")
        else:
            sobra = promedio - promedio_dese
            t_resultados.insert(INSERT, f"Has superado el promedio deseado por {sobra}.")
    
    else:
       t_resultados.insert(INSERT, "Debe seleccionar una opción")


#Datos medicos 
def datos():
    t = (tempe.get())
    p= float(peso.get())
    a = float(altur.get())
    IMC = p/ a**2
    barra = cmb_de.get()
    if barra == "IMC":
        d = IMC
        t_resultados2.insert(INSERT, (f"\n"f"Este es tu IMC {d}"))
    elif barra == "Alergia":
        e = t
        t_resultados2.insert(INSERT, f"El estudiante indica tener alergia a {e}.")
    else:
       t_resultados2.insert(INSERT, "Debe seleccionar una opción")

    

#Para que me salga elevado los datos del estudiante
def abrir_toplevel_centigrados():
    global toplevel_centigrados
    toplevel_centigrados = Toplevel()
    toplevel_centigrados.title("Promedio")
    toplevel_centigrados.resizable(False, False)
    toplevel_centigrados.geometry("400x300")
    toplevel_centigrados.config(bg="aquamarine2")

    # logo de la app
    lb_logo2 = Label(toplevel_centigrados, image=studen, bg="aquamarine2")
    lb_logo2.place(x=40,y=90)

    # etiqueta para valor en centigrados
    lb_note = Label(toplevel_centigrados, text = "Nota = ")
    lb_note.config(bg="aquamarine2", fg="black", font=('Gabriola', 18))
    lb_note.place(x=120, y=50)
    lb_note2 = Label(toplevel_centigrados, text = "Nota = ")
    lb_note2.config(bg="aquamarine2", fg="black", font=('Gabriola', 18))
    lb_note2.place(x=120, y=90)
    lb_note3= Label(toplevel_centigrados, text = "Nota = ")
    lb_note3.config(bg="aquamarine2", fg="black", font=('Gabriola', 18))
    lb_note3.place(x=120, y=130)
    lb_promediodese = Label(toplevel_centigrados, text = "Promedio deseado=  ")
    lb_promediodese.config(bg="aquamarine2", fg="black", font=('Gabriola', 18))
    lb_promediodese.place(x=60, y=170) 
    


    # caja de texto para valor en centigrados
    entry_note = Entry(toplevel_centigrados, textvariable=note)
    entry_note.config(bg="medium aquamarine", fg="black", font=("Candara", 12), width=6)
    entry_note.focus_set()
    entry_note.place(x=210,y=60)
    entry_note2 = Entry(toplevel_centigrados, textvariable=note2)
    entry_note2.config(bg="medium aquamarine", fg="black", font=("Candara", 12), width=6)
    entry_note2.place(x=210,y=100)
    entry_note3 = Entry(toplevel_centigrados, textvariable=note3)
    entry_note3.config(bg="medium aquamarine", fg="black", font=("Candara", 12), width=6)
    entry_note3.place(x=210,y=140)
    entry_promediodese= Entry(toplevel_centigrados, textvariable=promedio_deseado)
    entry_promediodese.config(bg="medium aquamarine", fg="black", font=("Candara", 12), width=6)
    entry_promediodese.place(x=210,y=140)
    entry_promediodese.config(bg="medium aquamarine", fg="black", font=("Candara", 12), width=6)
    entry_promediodese.place(x=210,y=180)

    #enter para las notas

    entry_note.bind("<Return>", lambda event: entry_note2.focus_set())
    entry_note2.bind("<Return>", lambda event: entry_note3.focus_set())
    entry_note3.bind("<Return>", lambda event: entry_promediodese.focus_set())
# boton para convertir
    bt_aceptar1 = Button(toplevel_centigrados,text="Aceptar", command=aceptar1)
    bt_aceptar1.place(x=100, y=240, width=100, height=30)

# aceptar
def aceptar1():
    global nota
    nota = int(note2.get())
    toplevel_centigrados.destroy()
#Datos para el informe medico
def abrir_toplevel_informe():
    global toplevel_informe
    toplevel_informe = Toplevel()
    toplevel_informe.title("Tu salud")
    toplevel_informe.resizable(False, False)
    toplevel_informe.geometry("400x250")
    toplevel_informe.config(bg="aquamarine2")

    # logo de la app
    lb_logo2 = Label(toplevel_informe, image=doc, bg="aquamarine2")
    lb_logo2.place(x=10,y=10)

    # etiqueta para valor en centigrados
    lb_temp = Label(toplevel_informe, text = "alergia")
    lb_temp.config(bg="aquamarine2", fg="black", font=('Gabriola', 18))
    lb_temp.place(x=100, y=50)
    lb_peso= Label(toplevel_informe, text = "Peso")
    lb_peso.config(bg="aquamarine2", fg="black", font=('Gabriola', 18))
    lb_peso.place(x=120, y=100)
    lb_altur= Label(toplevel_informe, text = "Altura")
    lb_altur.config(bg="aquamarine2", fg="black", font=('Gabriola', 18))
    lb_altur.place(x=120, y=140)

    # caja de texto para valor en centigrados
    entry_temp = Entry(toplevel_informe, textvariable=tempe)
    entry_temp.config(bg="medium aquamarine", fg="black", font=("Candara", 12), width=8)
    entry_temp.focus_set()
    entry_temp.place(x=210,y=60)
    entry_peso = Entry(toplevel_informe, textvariable=peso)
    entry_peso.config(bg="medium aquamarine", fg="black", font=("Candara", 12), width=6)
    entry_peso.focus_set()
    entry_peso.place(x=210,y=100)
    entry_altur = Entry(toplevel_informe, textvariable=altur)
    entry_altur.config(bg="medium aquamarine", fg="black", font=("Candara", 12), width=6)
    entry_altur.focus_set()
    entry_altur.place(x=210,y=140)
    # boton para convertir
    bt_aceptar = Button(toplevel_informe,text="Aceptar", command=aceptar)
    bt_aceptar.place(x=100, y=200, width=100, height=30)

    #enter para las notas

    entry_temp.bind("<Return>", lambda event: entry_peso.focus_set())
    entry_peso.bind("<Return>", lambda event: entry_altur.focus_set())
    
# aceptar
def aceptar():
    global cent
    cent = tempe.get()
    toplevel_informe.destroy()
   
 # salir
def salir():
    messagebox.showinfo("Ayudate", "La app se va a cerrar")
    ventana_principal.destroy()   


# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = tk.Tk()

# titulo de la ventana
ventana_principal.title("Ayudate")


# tamaño de la ventana
ventana_principal.geometry("700x700")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="aquamarine2")

# boton para salir
saliricon = PhotoImage(file="img/salir1.png")
bt_salir = Button(ventana_principal,text="Salir", image=saliricon, command=salir)
bt_salir.place(x=650, y=660, width=50, height=42)

# Crear segunda ventana
top = tk.Toplevel()
ventana_principal.lift()
top.title("Estudiante")
# ---------------------------------------------------------
#Lo que va a ver en el top
#------------------------------------------------------
top.geometry("350x300")
top.resizable(False, False)
top.config(bg="aquamarine2")
usuar = StringVar()
code = StringVar()
frame_top = Frame(top)
frame_top.config(bg="aquamarine2", width=399, height=300)
frame_top.place(x=0, y=0)
def aceptar2(): 
    
    (usuar.get())
    top.destroy()
bt_aceptar = Button(frame_top,text="Aceptar", command=aceptar2)
bt_aceptar.place(x=100, y=220, width=100, height=30)

#imagen
studen1 = PhotoImage(file="img/estudiante.png")
lb_studen = Label(frame_top, image=studen1, bg="aquamarine2")
lb_studen.place(x=20,y=40)
lb_usuar = Label(frame_top, text = "Usuario")
lb_usuar.config(bg="aquamarine2", fg="black", font=('Gabriola', 20))
lb_usuar.place(x=100, y=50)
entry_usuar = Entry(frame_top)
entry_usuar.config(bg="medium aquamarine", fg="black", font=("Candara", 12), width=24)
entry_usuar.focus_set()
entry_usuar.place(x=100, y= 100)
lb_code = Label(frame_top, text = "Codigo")
lb_code.config(bg="aquamarine2", fg="black", font=('Gabriola', 20))
lb_code.place(x=100, y=130)
entry_code = Entry(frame_top)
entry_code.config(bg="medium aquamarine", fg="black", font=("Candara", 12), width=24)
entry_code.focus_set()
entry_code.place(x=100, y= 180)
#--------------------------------
# frame entrada datos
#--------------------------------

note = StringVar()
note2 = StringVar()
note3 = StringVar()
promedio_deseado= StringVar()
tempe= StringVar()
peso= StringVar()
altur= StringVar()
kf = ["Promedio", "Promedio deseado"]
kf_selected = StringVar()
de = ["IMC", "Alergia"]
de_selected= StringVar()
global logo
#Datos academicos de estudiante
#--------------------------
frame_academi = Frame(ventana_principal)
frame_academi.config(bg="white", width=330, height=600)
frame_academi.place(x=360, y=10)


#imagen
studen = PhotoImage(file="img/estudiante.png")
lb_studen = Label(frame_academi, image=studen, bg="white")
lb_studen.place(x=20,y=40)

# boton para abrir Toplevel para ingresar °C
bt_centigrados = Button(frame_academi, text="Ingresar Notas", command=abrir_toplevel_centigrados)
bt_centigrados.place(x=150, y=60)
#Lista para las notas
#-------------------------------
cmb_kf = ttk.Combobox(frame_academi, textvariable=kf_selected, values=kf, font=("Fixedsys", 12))
cmb_kf.place(x=30, y=110)
# boton para convertir
bt_convertir = Button(frame_academi,text="Convertir", command=convertir)
bt_convertir.place(x=45, y=200, width=100, height=30)


#--------------------------------
# frame resultados
#--------------------------------
frame_resultados = Frame(frame_academi)
frame_resultados.config(bg="white", width=480, height=180)
frame_resultados.place(x=10, y=310)

# area de texto para los resultados
t_resultados = Text(frame_resultados)
t_resultados.config(bg="black", fg="green yellow", font=("Courier", 18))
t_resultados.place(x=0,y=30,width=310,height=130)


#---------------------
#Datos medicos
frame_medic= Frame(ventana_principal)
frame_medic.config(bg="white", width=330, height=600)
frame_medic.place(x=10, y=10)
doc = PhotoImage(file="img/doctor.png")
lb_doc = Label(frame_medic, image=doc, bg="white")
lb_doc.place(x=20,y=40)
# boton para abrir Toplevel para ingresar °C
bt_informe = Button(frame_medic, text="Ingresar informe", command=abrir_toplevel_informe)
bt_informe.place(x=150, y=60)

cmb_de = ttk.Combobox(frame_medic, textvariable=de_selected, values=de, font=("Fixedsys", 12))
cmb_de.place(x=30, y=110)

# boton para convertir
bt_convertir = Button(frame_medic,text="Convertir", command=datos)
bt_convertir.place(x=45, y=200, width=100, height=30)

#--------------------------------
# frame resultados
#--------------------------------
frame_resultados2 = Frame(frame_medic)
frame_resultados2.config(bg="white", width=480, height=180)
frame_resultados2.place(x=10, y=310)

# area de texto para los resultados
t_resultados2 = Text(frame_resultados2)
t_resultados2.config(bg="black", fg="green yellow", font=("Courier", 18))
t_resultados2.place(x=0,y=30,width=310,height=130)



# se ejecuta el metodo mainloop() de la clase Tk() a través de la instancia ventana_principal. Este metodo despliega la ventana en pantalla y queda a la espera de lo que el usuario haga (click en un boton, escribir, etc).  Cada acción del usuario se conoce como un evento.  El método mainloop() es un bucle infinito.
ventana_principal.mainloop()


