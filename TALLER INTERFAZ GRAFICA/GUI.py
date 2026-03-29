import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame
import os



# Ventana principal
ventana = tk.Tk()
ventana.title("Interfaz Gráfica - Proyecto Tkinter")
ventana.geometry("620x520")
ventana.resizable(False, False)

# Frame principal 
main_frame = tk.Frame(ventana, bg="#227AFF")
main_frame.pack(fill=tk.BOTH, expand=True)

#ANÁLISIS DE NÚMEROS 
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

#VENTANA ANÁLISIS DE NÚMEROS
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




#Botón en la ventanaa principal para abrir análisis de pares
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

#Botón para abrir ficha personal
def abrir_ficha_personal():
    top = tk.Toplevel(ventana)
    top.title("Ficha Personal")
    top.geometry("580x640")
    fondoo=Image.open('Fondo ficha personal.jpg').resize((580,640))
    fondoo_final=ImageTk.PhotoImage(fondoo)
    top.image = fondoo_final
    fondo = tk.Label(top, image=top.image)
    fondo.place(x=0, y=0, relwidth=1, relheight=1)     
    
    def abrir_ficha_personal():
        top = tk.Toplevel(ventana)
        top.title("Ficha Personal")
        top.geometry("580x640")
        

    


    #Imagenes de ficha personal
    img_fondo_pil = Image.open("Fondo ficha personal.jpg").resize((580, 640))
    top.imagen_fondo = ImageTk.PhotoImage(img_fondo_pil) 
    label_fondo = tk.Label(top, image=top.imagen_fondo)
    label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

    img_yo_pil = Image.open('FICHA PERSONAL YO.jpeg').resize((180, 150))
    top.imagen_perfil = ImageTk.PhotoImage(img_yo_pil)
    label_foto_perfil = tk.Label(top, image=top.imagen_perfil)
    label_foto_perfil.place(x=380, y=235) 
    
    img_mapa_pil = Image.open('mapa.jpg').resize((160, 110)) 
    top.imagen_mapa = ImageTk.PhotoImage(img_mapa_pil)
    label_mapa = tk.Label(top, image=top.imagen_mapa)
    label_mapa.place(x=130, y=390)

    img_rawayana_pil = Image.open('RAWAYANAjpg.jpg').resize((150, 125))
    top.imagen_rawayana = ImageTk.PhotoImage(img_rawayana_pil)
    label_rawayana = tk.Label(top, image=top.imagen_rawayana)
    label_rawayana.place(x=400, y=500)



# Parar detener la música
    def detener_musica_auto():
        pygame.mixer.music.stop()
        print("Límite de 10 segundos alcanzado.")

    # Para reproducir
    def reproducir_musica():
        try:
            if not pygame.mixer.get_init():
                pygame.mixer.init()
            pygame.mixer.music.load("CANEY.mp3") 
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play()
           

            # Detener a los 10s
            top.after(10000, detener_musica_auto)
        except Exception as e:
            print(f"Error: {e}")

    #Boton musica
    boton_musica = tk.Button(
        top,
        text="▶ PLAY RAWAYANA",
        command=reproducir_musica,
        bg="#FFD700",
        fg="black",
        font=("Arial", 10, "bold")
    )
    boton_musica.place(x=411, y=410)
    

#Información ficha personal
    label_nombre = tk.Label(
        top, 
        text="VICTORIA SOFÍA FERNÁNDEZ MARTÍNEZ",
        font=("Arial", 11, "bold"),
        bg="#ffffff", 
        fg="Black"
    )
    label_nombre.pack(anchor="center",pady=20)


    label_edad_carnet =tk.Label(
        top,
        text=" Carnet: 2026120151    Edad: 18 años",
        wraplength=100,
        font=("Arial", 12, "bold"),
        bg="#ffffff",
        fg="Black"
    )
    label_edad_carnet.pack(anchor="w", padx=10)

    texto_bio = "Biografía:Soy venezolana y me mudé a Costa Rica a los 7 años, soy muy sociable y me parece interesante el tema de tecnología por ende decidí estudiar ingeniería en computadores en el TEC, actualmente juego voleibol en el equipo universitario y vivo en Cartago."
    label_bio = tk.Label(
    top, 
    text=texto_bio, 
    font=("Arial", 11,"bold" ), 
    bg="#f5e042", 
    fg="Black",
    wraplength=300,  
    justify="left"
)
    label_bio.place(x=142, y=60)

    label_musica=tk.Label(
     top,
        text="Funky/Reggae   Rawayana",
        wraplength=120,
        font=("Arial", 10, "bold"),
        bg="#ffffff",
        fg="Black"   
    )
    label_musica.place(x=432, y=450)
    


# Botón en la ventana principal para la FICHA PERSONAL 
boton_ficha = tk.Button( 
    ventana,
    text="Ficha personal", 
    command=abrir_ficha_personal, 
    bg="#DB351F",
    fg="white",
    activebackground="#C21616",
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
    
    frame = tk.Frame(top,)
    frame.pack(fill=tk.BOTH, expand=True)
    boton_ficha.place(x=186,y=200)


def abrir_ficha_personal():
    top = tk.Toplevel(ventana)  
    top.title("Ficha Personal")
    top.geometry("580x640")

#Animación de esferas 
def abrir_animacion():
    top = tk.Toplevel(ventana)
    top.title("Animación de Esferas")
    top.geometry("580x640")
    top.configure(bg="#227AFF")


    #Control de Velocidad 
    tk.Label(top, text="Ajustar Velocidad:", bg="#227AFF", fg="white").pack()
    control_vel = tk.Scale(top, from_=1, to=10, orient="horizontal")
    control_vel.set(3)
    control_vel.pack(pady=5)
    canvas = tk.Canvas(top, width=400, height=300, bg="black")
    canvas.pack(pady=20)

    #Las esferas
    bola1 = canvas.create_oval(10, 10, 40, 40, fill="red")
    bola2 = canvas.create_oval(350, 250, 380, 280, fill="yellow")

    # 4. Variables de dirección 
    
    vx1 = [1] 
    vy1 = [1]  
    vx2 = [-1]
    vy2 = [-1]

    def mover_esferas():
       #Para obteener la velocidad
        v = control_vel.get()
        
        pos1 = canvas.coords(bola1)
        pos2 = canvas.coords(bola2)

        #Rebostes bola1
        if pos1[0] <= 0 or pos1[2] >= 400:
            vx1[0] *= -1
        if pos1[1] <= 0 or pos1[3] >= 300:
            vy1[0] *= -1

        #Rebotes bola2
        if pos2[0] <= 0 or pos2[2] >= 400:
            vx2[0] *= -1
        if pos2[1] <= 0 or pos2[3] >= 300:
            vy2[0] *= -1

        #Rebotes entre ellas
        if abs(pos1[0] - pos2[0]) < 30 and abs(pos1[1] - pos2[1]) < 30:
            vx1[0] *= -1
            vy1[0] *= -1
            vx2[0] *= -1
            vy2[0] *= -1

        #Mover las bolas
        canvas.move(bola1, v * vx1[0], v * vy1[0])
        canvas.move(bola2, v * vx2[0], v * vy2[0])

        #Repetir el movimiento
        top.after(20, mover_esferas)

    #Iniciar
    mover_esferas()

    #Botón para cerrar
    tk.Button(top, text="VOLVER", command=top.destroy).pack(pady=10)




boton_abrir_anim = tk.Button( 
    ventana,               
    text="Animación", 
    command=abrir_animacion, 
    bg="#B5220F",          
    fg="white",
    activebackground="#7D0B0B",
    activeforeground="white",
    font=("Arial", 12, "bold"),
    width=24,
    height=2
)


boton_abrir_anim.place(x=186, y=400)


ventana.mainloop()




             