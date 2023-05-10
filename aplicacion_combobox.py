import tkinter as tk

# Crear ventana principal
root = tk.Tk()
root.title("Ventana principal")

# Crear segunda ventana
top = tk.Toplevel()
top.title("Ventana encima")
top.lift()

# Ejecutar programa
root.mainloop()


