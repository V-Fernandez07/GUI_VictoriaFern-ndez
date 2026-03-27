import tkinter as tk
from tkinter import messagebox

# Ventana principal
ventana = tk.Tk()
ventana.title("Interfaz Gráfica - Proyecto Tkinter")
ventana.geometry("620x520")
ventana.configure(bg="#24cde7")
ventana.resizable(False, False)

# Frame principal con fondo visible
main_frame = tk.Frame(ventana, bg="#24cde7")
main_frame.pack(fill=tk.BOTH, expand=True)

# ============== 1. ANÁLISIS DE NÚMEROS (RECURSIVO) ==============

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


def abrir_analisis_numeros():
    top = tk.Toplevel(ventana)
    top.title("Análisis de Números")
    top.geometry("420x280")
    top.resizable(False, False)

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

# Botón en la ventana principal para abrir análisis de pares
boton_analisis = tk.Button(
    main_frame,
    text="Abrir Análisis de Pares",
    command=abrir_analisis_numeros,
    bg="#FF6B6B",
    fg="white",
    activebackground="#D12B4D",
    activeforeground="white",
    font=("Arial", 12, "bold"),
    width=24,
    height=2
)
boton_analisis.pack(pady=22)

ventana.mainloop()
