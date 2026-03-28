import tkinter as tk
from tkinter import messagebox

# Ventana principal
ventana = tk.Tk()
ventana.title("Interfaz Gráfica - Proyecto Tkinter")
ventana.geometry("620x520")
ventana.resizable(False, False)

# ============== 1. ANÁLISIS DE NÚMEROS (RECURSIVO) ==============

def encontrar_pares(n, a=1, pares=None):
    """Función recursiva de un único método para hallar pares de factores."""
    if pares is None:
        pares = []
    if a * a > n:
        return pares
    if n % a == 0:
        b = n // a
        if a <= b:
            pares.append((a, b))
    return encontrar_pares(n, a + 1, pares)


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
                return
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

# ============== 2. FICHA PERSONAL ==============

def abrir_ficha_personal():
    top = tk.Toplevel(ventana)
    top.title("Ficha Personal")
    top.geometry("580x640")
    top.resizable(False, False)

    frame = tk.Frame(top, bg="white")
    frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    tk.Label(frame, text="FICHA PERSONAL", font=("Arial", 16, "bold"), bg="white").pack(pady=12)

    datos = [
        ("Nombre:", "Juan Carlos Pérez López"),
        ("Carnet:", "12345678"),
        ("Edad:", "20 años"),
        ("Género musical:", "Rock/Pop"),
        ("Grupo favorito:", "The Beatles"),
    ]

    for etiqueta, valor in datos:
        sub = tk.Frame(frame, bg="white")
        sub.pack(fill=tk.X, pady=4)
        tk.Label(sub, text=etiqueta, font=("Arial", 10, "bold"), width=14, anchor="w", bg="white").pack(side=tk.LEFT)
        tk.Label(sub, text=valor, font=("Arial", 10), anchor="w", bg="white").pack(side=tk.LEFT, fill=tk.X, expand=True)

    tk.Label(frame, text="Biografía (máximo 2 párrafos):", font=("Arial", 10, "bold"), bg="white").pack(pady=(12, 2), anchor='w')
    bio = tk.Text(frame, height=5, font=("Arial", 10), wrap=tk.WORD)
    bio.insert(tk.END, "Soy apasionado por la programación, los algoritmos recursivos y el desarrollo de interfaces.\n\nMe gusta practicar con Python y Tkinter para realizar proyectos.")
    bio.config(state=tk.DISABLED)
    bio.pack(fill=tk.X, pady=2)

    tk.Label(frame, text="(Imágenes no incluidas en el ejemplo).", font=("Arial", 9, "italic"), bg="white").pack(pady=12)

# ============== 3. ANIMACIÓN DE ESFERAS ==============

def mover_esfera(esfera, ancho, alto):
    esfera['x'] += esfera['vx']
    esfera['y'] += esfera['vy']

    if esfera['x'] - esfera['radio'] <= 0 or esfera['x'] + esfera['radio'] >= ancho:
        esfera['vx'] = -esfera['vx']
        if esfera['x'] - esfera['radio'] < 0:
            esfera['x'] = esfera['radio']
        if esfera['x'] + esfera['radio'] > ancho:
            esfera['x'] = ancho - esfera['radio']

    if esfera['y'] - esfera['radio'] <= 0 or esfera['y'] + esfera['radio'] >= alto:
        esfera['vy'] = -esfera['vy']
        if esfera['y'] - esfera['radio'] < 0:
            esfera['y'] = esfera['radio']
        if esfera['y'] + esfera['radio'] > alto:
            esfera['y'] = alto - esfera['radio']


def colision_esferas(e1, e2):
    dx = e1['x'] - e2['x']
    dy = e1['y'] - e2['y']
    dist2 = dx*dx + dy*dy
    radios = e1['radio'] + e2['radio']
    if dist2 < radios*radios:
        e1['vx'], e2['vx'] = e2['vx'], e1['vx']
        e1['vy'], e2['vy'] = e2['vy'], e1['vy']


def abrir_animacion():
    top = tk.Toplevel(ventana)
    top.title("Animación de Esferas")
    top.geometry("700x620")
    top.resizable(False, False)

    control_frame = tk.Frame(top, bg="#f0f0f0")
    control_frame.pack(fill=tk.X, pady=5)
    tk.Label(control_frame, text="Velocidad:", font=("Arial", 10, "bold"), bg="#f0f0f0").pack(side=tk.LEFT, padx=5)

    velocidad_var = tk.IntVar(value=3)
    velocidad_scale = tk.Scale(control_frame, from_=1, to=10, orient=tk.HORIZONTAL, variable=velocidad_var,
                               bg="#f0f0f0", length=250)
    velocidad_scale.pack(side=tk.LEFT, padx=5)

    canvas_anim = tk.Canvas(top, bg="white", width=690, height=520)
    canvas_anim.pack(padx=5, pady=5)

    esfera1 = {'x': 100, 'y': 100, 'radio': 20, 'color': 'red', 'vx': 3, 'vy': 2}
    esfera2 = {'x': 465, 'y': 350, 'radio': 20, 'color': 'blue', 'vx': -2, 'vy': -3}

    activo = {'value': True}

    def animar():
        if not activo['value']:
            return

        factor = velocidad_var.get() / 3.0
        if factor <= 0:
            factor = 1

        esfera1['vx'] = 3 * (1 if esfera1['vx'] >= 0 else -1) * factor
        esfera1['vy'] = 2 * (1 if esfera1['vy'] >= 0 else -1) * factor
        esfera2['vx'] = 2 * (1 if esfera2['vx'] >= 0 else -1) * factor
        esfera2['vy'] = 3 * (1 if esfera2['vy'] >= 0 else -1) * factor

        mover_esfera(esfera1, 690, 520)
        mover_esfera(esfera2, 690, 520)
        colision_esferas(esfera1, esfera2)

        canvas_anim.delete("all")
        canvas_anim.create_oval(esfera1['x'] - esfera1['radio'], esfera1['y'] - esfera1['radio'],
                                esfera1['x'] + esfera1['radio'], esfera1['y'] + esfera1['radio'],
                                fill=esfera1['color'], outline="black")
        canvas_anim.create_oval(esfera2['x'] - esfera2['radio'], esfera2['y'] - esfera2['radio'],
                                esfera2['x'] + esfera2['radio'], esfera2['y'] + esfera2['radio'],
                                fill=esfera2['color'], outline="black")

        canvas_anim.after(30, animar)

    def cerrar_animacion():
        activo['value'] = False
        top.destroy()

    top.protocol("WM_DELETE_WINDOW", cerrar_animacion)
    animar()

# ============== MENÚ PRINCIPAL ==============

main_frame = tk.Frame(ventana, bg="#E8F4FF")
main_frame.pack(fill=tk.BOTH, expand=True)

tk.Label(main_frame, text="MENÚ PRINCIPAL", font=("Arial", 20, "bold"), bg="#E8F4FF").pack(pady=18)

for texto, comando, color in [
    ("1. Análisis de Números", abrir_analisis_numeros, "#FF6B6B"),
    ("2. Ficha Personal", abrir_ficha_personal, "#4ECDC4"),
    ("3. Animación de Esferas", abrir_animacion, "#45B7D1"),
]:
    tk.Button(main_frame, text=texto, command=comando, font=("Arial", 12, "bold"),
              bg=color, fg="white", width=26, height=2).pack(pady=8)

ventana.mainloop()
