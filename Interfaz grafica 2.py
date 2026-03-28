import tkinter as tk
ventana=tk.Tk ()
ventana.title("interfaz grafica")
ventana.geometry ("500x500")
def cerrarventana():
    ventana=tk.Toplevel
    ventana.title("bb")
ventana.resizable(width=True, height=True)
canva1=tk.Canvas (ventana, bg='purple', width= 3840, height= 2160)
canva1.pack()

root = tk.Tk (useTk=ventana)
root.title ("Interfaz gráfica")
root.geometry ("500x500")
root.resizable(False, False)
texto = tk. Text (root, height=5, width=40)
texto.insert("1.0", "Escribe aquí...")
texto.pack (pady=0)
canva1=tk.Canvas (root, bg='purple', width= 3840, height= 2160)
canva1.pack()
def leer_texto ():
    print ("Contenido:",texto.get("1.0", "end") )
    boton = tk.Button (root, text="Leer Texto", command=leer_texto)
    boton.place(x=250, y=250, anchor= 'center')
    boton.pack()
    def cerrar ():
        print("La aplicación se está cerrando...")
        root.destroy()
        


ventana.mainloop()