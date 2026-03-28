import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame


# Ventana principal
ventana = tk.Tk()
ventana.title("Interfaz Gráfica - Proyecto Tkinter")
ventana.geometry("620x520")
ventana.resizable(False, False)

# Frame principal 
main_frame = tk.Frame(ventana, bg="#5995FB")
main_frame.pack(fill=tk.BOTH, expand=True)

# 1. ANÁLISIS DE NÚMEROS 

def encontrar_pares(n, a=1, pares=None):
    """Función recursiva para hallar pares de factores."""
    if pares is None:
        pares = []
    if a * a > n:
        return pares
    if n % a == 0:
        b = n // a
        if a <= b:
            pares.append((a, b))
    return encontrar_pares(n, a + 1, pares)
print (encontrar_pares (10))

# VENTANA ANÁLISIS DE NÚMEROS
def abrir_analisis_numeros():
    top = tk.Toplevel(ventana)
    top.title("Análisis de Números")
    top.geometry("420x280")

    mi_foto = Image.open('Mariovic.jpg').resize((420, 280))
    foto_final = ImageTk.PhotoImage(mi_foto)
    top.image = foto_final
    fondo = tk.Label(top, image=top.image)
    fondo.place(x=0, y=0, relwidth=1, relheight=1)

    tk.Label(top, text="Ingresa un número entero positivo:", font=("Arial", 11)).pack(pady=8)
    entry = tk.Entry(top, font=("Arial", 12), width=22)
    entry.pack(pady=5)

    resultado_text = tk.Text(top, height=8, width=48, font=("Arial", 10))
    resultado_text.pack(pady=8)

    

    def calcular():
        try:
            num = int(entry.get())
            if num <= 0:
                messagebox.showerror("Error", "Debe ser un número positivo")
                return "error"
            pares = encontrar_pares(num)
            resultado_text.config(state=tk.NORMAL)
            resultado_text.delete(1.0, tk.END)
            resultado_text.insert(tk.END, f"Número: {num}\n\n")
            if not pares:
                resultado_text.insert(tk.END, "No se encontraron pares de factores positivos.\n")
            else:
                resultado_text.insert(tk.END, "Pares encontrados:\n")
                for a, b in pares:
                    resultado_text.insert(tk.END, f"  ({a}, {b})\n")
            resultado_text.config(state=tk.DISABLED)
        except ValueError:
            messagebox.showerror("Error", "Ingresa un número válido")

    tk.Button(top, text="Calcular", command=calcular, bg="#4CAF50", fg="white", font=("Arial", 10), width=16).pack(pady=8)

# Botón en la ventan(a principal para abrir análisis de pares
boton_analisis = tk.Button(
main_frame,
text="Abrir Análisis de Pares",
command=abrir_analisis_numeros,
bg="#F05B3E",    fg="white",
activebackground="#D12B4D",
activeforeground="white",
font=("Arial", 12, "bold"),
width=24,
height=2)

boton_analisis.pack(pady=22)


# Botón en la ventana principal para la FICHA PERSONAL 

def abrir_ficha_personal():
    top = tk.Toplevel(ventana)
    top.title("Ficha Personal")
    top.geometry("580x640")
    fondoo=Image.open('Fondo ficha personal.jpg').resize((580,640))
    fondoo_final=ImageTk.PhotoImage(fondoo)
    top.image = fondoo_final
    fondo = tk.Label(top, image=top.image)
    fondo.place(x=0, y=0, relwidth=1, relheight=1)


boton_ficha = tk.Button( 
    ventana,
    text="Ficha personal", 
    command=abrir_ficha_personal, 
    bg="#F05B3E",
    fg="white",
    activebackground="#D12B4D",
    activeforeground="white",
    font=("Arial", 12, "bold"),
    width=24,
    height=2
)
boton_ficha.place(x=186,y=200)
def abrir_ficha_personal():
    top = tk.Toplevel(ventana)
    top.title("Ficha Personal")
    top.geometry("580x640")
    
    frame = tk.Frame(top, bg="#f542c8")
    frame.pack(fill=tk.BOTH, expand=True)

    # TITULO (Indentado con Tab)
    tk.Label(top, text="Ficha personal", font=("Arial", 16, "bold"), 
             bg="white").pack(pady=20)

    # DATOS (Todos indentados para que existan dentro de 'frame')
    tk.Label(top, text="Nombre: Victoria Sofía Fernández Martínez",
             font=("Arial", 12, "bold"), bg="#f542c8", fg="white").pack(anchor="w", padx=50, pady=10)

    tk.Label(top, text="Carnet: 2026121151",
             font=("Arial", 12, "bold"), bg="#f542c8", fg="white").pack(anchor="w", padx=50, pady=10)

    tk.Label(top, text="Edad: 18 años",
             font=("Arial", 12, "bold"), bg="#f542c8", fg="white").pack(anchor="w", padx=50, pady=10)

    tk.Label(top, text="Género musical: Reggae/Funky",
             font=("Arial", 12, "bold"), bg="#f542c8", fg="white").pack(anchor="w", padx=50, pady=10)

    tk.Label(top, text="Grupo favorito: Rawayana",
             font=("Arial", 12, "bold"), bg="#f542c8", fg="white").pack(anchor="w", padx=50, pady=10)


boton_ficha = tk.Button(ventana, text="Ficha personal", command=abrir_ficha_personal, 
                        bg="#F05B3E", fg="white", font=("Arial", 12, "bold"), 
                        width=24, height=2)
boton_ficha.place(x=186, y=200)

ventana.mainloop()




             