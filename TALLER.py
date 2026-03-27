import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import random
import math
from pathlib import Path
from datetime import datetime

class AnalisisNumeros:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Análisis de Números - Pares Divisores")
        self.ventana.geometry("500x400")
        self.ventana.configure(bg='#f0f0f0')
        
        # Título
        titulo = tk.Label(self.ventana, text="Análisis de Números", 
                         font=('Arial', 16, 'bold'),
                         bg='#f0f0f0')
        titulo.pack(pady=10)
        
        # Frame de entrada
        frame_entrada = ttk.LabelFrame(self.ventana, text="Ingrese un número entero positivo")
        frame_entrada.pack(pady=10, padx=20, fill='x')
        
        self.entry_numero = ttk.Entry(frame_entrada, font=('Arial', 12), width=30)
        self.entry_numero.pack(pady=10, padx=10)
        
        # Botón calcular
        btn_calcular = ttk.Button(self.ventana, text="Calcular Pares", 
                                 command=self.calcular_pares)
        btn_calcular.pack(pady=10)
        
        # Frame de resultados
        frame_resultados = ttk.LabelFrame(self.ventana, text="Pares Divisores (a, b) donde a × b = n")
        frame_resultados.pack(pady=10, padx=20, fill='both', expand=True)
        
        # Área de texto con scrollbar
        scrollbar = ttk.Scrollbar(frame_resultados)
        scrollbar.pack(side='right', fill='y')
        
        self.text_resultados = tk.Text(frame_resultados, height=12, width=50, 
                                       yscrollcommand=scrollbar.set, 
                                       font=('Arial', 10))
        self.text_resultados.pack(pady=10, padx=10, fill='both', expand=True)
        scrollbar.config(command=self.text_resultados.yview)
    
    def encontrar_pares_recursivo(self, n, divisor=1, pares=None):
        """
        Algoritmo recursivo que encuentra todos los pares (a, b) donde a × b = n
        """
        if pares is None:
            pares = []
        
        # Caso base: cuando divisor² > n, hemos encontrado todos los pares
        if divisor * divisor > n:
            return pares
        
        # Si divisor divide a n, añadimos el par
        if n % divisor == 0:
            pares.append((divisor, n // divisor))
        
        # Llamada recursiva con el siguiente divisor
        return self.encontrar_pares_recursivo(n, divisor + 1, pares)
    
    def calcular_pares(self):
        """Calcula y muestra los pares divisores"""
        self.text_resultados.delete(1.0, tk.END)
        
        try:
            numero = int(self.entry_numero.get())
            
            if numero <= 0:
                self.text_resultados.insert(tk.END, "Error: Ingrese un número entero positivo")
                return
            
            # Usar el algoritmo recursivo
            pares = self.encontrar_pares_recursivo(numero)
            
            if pares:
                self.text_resultados.insert(tk.END, f"Número ingresado: {numero}\n")
                self.text_resultados.insert(tk.END, f"Total de pares encontrados: {len(pares)}\n\n")
                self.text_resultados.insert(tk.END, "Pares (a, b):\n")
                self.text_resultados.insert(tk.END, "-" * 40 + "\n")
                
                for a, b in pares:
                    self.text_resultados.insert(tk.END, f"({a:6d}, {b:6d})  →  {a} × {b} = {numero}\n")
            else:
                self.text_resultados.insert(tk.END, "No se encontraron pares divisores")
                
        except ValueError:
            self.text_resultados.insert(tk.END, "Error: Ingrese un número entero válido")


class FichaPersonal:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Ficha Personal")
        self.ventana.geometry("700x900")
        self.ventana.configure(bg='#f0f0f0')
        
        # Variables para almacenar rutas de archivos
        self.ruta_foto_programador = None
        self.ruta_imagen_lugar = None
        self.ruta_foto_grupo = None
        self.ruta_cancion = None
        
        # Crear un canvas con scrollbar para el contenido
        canvas = tk.Canvas(self.ventana, bg='#f0f0f0', highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.ventana, orient='vertical', command=canvas.yview)
        
        frame_contenido = ttk.Frame(canvas)
        frame_contenido.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=frame_contenido, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # --- DATOS PERSONALES ---
        frame_personal = ttk.LabelFrame(frame_contenido, text="Datos Personales", padding=10)
        frame_personal.pack(pady=10, padx=10, fill='x')
        
        ttk.Label(frame_personal, text="Nombre:").grid(row=0, column=0, sticky='w', padx=5, pady=5)
        self.entry_nombre = ttk.Entry(frame_personal, width=40)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame_personal, text="Carnet:").grid(row=1, column=0, sticky='w', padx=5, pady=5)
        self.entry_carnet = ttk.Entry(frame_personal, width=40)
        self.entry_carnet.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(frame_personal, text="Edad:").grid(row=2, column=0, sticky='w', padx=5, pady=5)
        self.entry_edad = ttk.Entry(frame_personal, width=40)
        self.entry_edad.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(frame_personal, text="Biografía (máx. 2 párrafos):").grid(row=3, column=0, sticky='nw', padx=5, pady=5)
        self.text_biografia = tk.Text(frame_personal, width=40, height=5, font=('Arial', 10))
        self.text_biografia.grid(row=3, column=1, padx=5, pady=5)
        
        # --- DATOS MULTIMEDIA PERSONAL ---
        frame_multimedia = ttk.LabelFrame(frame_contenido, text="Fotografía del Programador", padding=10)
        frame_multimedia.pack(pady=10, padx=10, fill='x')
        
        self.label_foto_prog = ttk.Label(frame_multimedia, text="Sin imagen seleccionada", 
                                         background='#e0e0e0', width=30, height=5)
        self.label_foto_prog.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        
        btn_foto_prog = ttk.Button(frame_multimedia, text="Seleccionar Fotografía", 
                                   command=self.seleccionar_foto_programador)
        btn_foto_prog.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        
        # --- LUGAR DE RESIDENCIA ---
        frame_lugar = ttk.LabelFrame(frame_contenido, text="Lugar de Residencia", padding=10)
        frame_lugar.pack(pady=10, padx=10, fill='x')
        
        self.label_lugar = ttk.Label(frame_lugar, text="Sin imagen seleccionada", 
                                     background='#e0e0e0', width=30, height=5)
        self.label_lugar.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        
        btn_lugar = ttk.Button(frame_lugar, text="Seleccionar Imagen/Mapa", 
                              command=self.seleccionar_imagen_lugar)
        btn_lugar.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        
        # --- GRUPO MUSICAL ---
        frame_musica = ttk.LabelFrame(frame_contenido, text="Grupo Musical Favorito", padding=10)
        frame_musica.pack(pady=10, padx=10, fill='x')
        
        ttk.Label(frame_musica, text="Nombre del Grupo/Intérprete:").grid(row=0, column=0, sticky='w', padx=5, pady=5)
        self.entry_grupo = ttk.Entry(frame_musica, width=40)
        self.entry_grupo.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame_musica, text="Género Musical:").grid(row=1, column=0, sticky='w', padx=5, pady=5)
        self.entry_genero = ttk.Entry(frame_musica, width=40)
        self.entry_genero.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(frame_musica, text="Fotografía del Grupo:").grid(row=2, column=0, sticky='w', padx=5, pady=5)
        self.label_foto_grupo = ttk.Label(frame_musica, text="Sin imagen seleccionada", 
                                          background='#e0e0e0', width=30, height=4)
        self.label_foto_grupo.grid(row=2, column=1, padx=5, pady=5)
        
        btn_foto_grupo = ttk.Button(frame_musica, text="Seleccionar Fotografía del Grupo", 
                                    command=self.seleccionar_foto_grupo)
        btn_foto_grupo.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        
        ttk.Label(frame_musica, text="Canción (10 segundos):").grid(row=4, column=0, sticky='w', padx=5, pady=5)
        self.label_cancion = ttk.Label(frame_musica, text="Sin archivo seleccionado", background='#e0e0e0')
        self.label_cancion.grid(row=4, column=1, padx=5, pady=5)
        
        btn_cancion = ttk.Button(frame_musica, text="Seleccionar Audio", 
                                command=self.seleccionar_cancion)
        btn_cancion.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
        
        # --- BOTONES FINALES ---
        frame_botones = ttk.Frame(frame_contenido)
        frame_botones.pack(pady=20, padx=10, fill='x')
        
        btn_guardar = ttk.Button(frame_botones, text="Guardar Ficha", command=self.guardar_ficha)
        btn_guardar.pack(side='left', padx=5)
        
        btn_cerrar = ttk.Button(frame_botones, text="Cerrar", command=self.ventana.destroy)
        btn_cerrar.pack(side='left', padx=5)
        
        # Empaquetar canvas y scrollbar
        canvas.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
    
    def seleccionar_foto_programador(self):
        archivo = filedialog.askopenfilename(
            title="Seleccionar fotografía del programador",
            filetypes=[("Imágenes", "*.png *.jpg *.jpeg *.gif"), ("Todos", "*.*")]
        )
        if archivo:
            self.ruta_foto_programador = archivo
            self.label_foto_prog.config(text=Path(archivo).name)
    
    def seleccionar_imagen_lugar(self):
        archivo = filedialog.askopenfilename(
            title="Seleccionar imagen o mapa del lugar",
            filetypes=[("Imágenes", "*.png *.jpg *.jpeg *.gif"), ("Todos", "*.*")]
        )
        if archivo:
            self.ruta_imagen_lugar = archivo
            self.label_lugar.config(text=Path(archivo).name)
    
    def seleccionar_foto_grupo(self):
        archivo = filedialog.askopenfilename(
            title="Seleccionar fotografía del grupo o intérprete",
            filetypes=[("Imágenes", "*.png *.jpg *.jpeg *.gif"), ("Todos", "*.*")]
        )
        if archivo:
            self.ruta_foto_grupo = archivo
            self.label_foto_grupo.config(text=Path(archivo).name)
    
    def seleccionar_cancion(self):
        archivo = filedialog.askopenfilename(
            title="Seleccionar archivo de audio (canción)",
            filetypes=[("Audio", "*.mp3 *.wav *.ogg *.flac"), ("Todos", "*.*")]
        )
        if archivo:
            self.ruta_cancion = archivo
            self.label_cancion.config(text=Path(archivo).name)
    
    def guardar_ficha(self):
        """Guarda la información de la ficha personal"""
        nombre = self.entry_nombre.get("Victoria Sofía Fernández Martínez")
        carnet = self.entry_carnet.get("2026120151")
        edad = self.entry_edad.get("18 años")
        biografia = self.text_biografia.get(1.0, tk.END)
        grupo = self.entry_grupo.get("RAWAYANA")
        genero = self.entry_genero.get("Reggae/Funk")
        
        if not all([nombre, carnet, edad, biografia.strip(), grupo, genero]):
            messagebox.showwarning("Datos Incompletos", "Por favor complete todos los campos de texto")
            return
        
        # Crear resumen
        resumen = f"""
╔═══════════════════════════════════════════════════════════╗
║              FICHA PERSONAL GUARDADA                     ║
╚═══════════════════════════════════════════════════════════╝

DATOS PERSONALES:
─────────────────
Nombre: {"Victoria Sofía Fernández Martínez"}
Carnet: {"2026120151"}
Edad: {"18 años"}

Biografía:
{"Soy venezolana y me mudé a Costa Rica a los 7 años, actualmente estoy estudiando ingeniería en computadores en el TEC y juego voleibol en el equipo de la universidad."}

MULTIMEDIA:
───────────
Fotografía del programador: {Path(self.ruta_foto_programador).name if self.ruta_foto_programador else 'No seleccionada'}
Lugar de residencia: {Path(self.ruta_imagen_lugar).name if self.ruta_imagen_lugar else 'No seleccionado'}

GRUPO MUSICAL FAVORITO:
──────────────────────
Grupo/Intérprete: {grupo}
Género: {genero}
Fotografía del grupo: {Path(self.ruta_foto_grupo).name if self.ruta_foto_grupo else 'No seleccionada'}
Canción: {Path(self.ruta_cancion).name if self.ruta_cancion else 'No seleccionada'}

Fecha de creación: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
        """
        
        messagebox.showinfo("Éxito", "Ficha personal guardada correctamente")


class Esfera:
    def __init__(self, canvas, x, y, radio, color, velocidad_x, velocidad_y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.radio = radio
        self.color = color
        self.vel_x = velocidad_x
        self.vel_y = velocidad_y
        self.id = canvas.create_oval(x - radio, y - radio, x + radio, y + radio, 
                                     fill=color, outline='')
    
    def mover(self, ancho, alto):
        # Actualizar posición
        self.x += self.vel_x
        self.y += self.vel_y
        
        # Rebote contra paredes
        if self.x - self.radio <= 0 or self.x + self.radio >= ancho:
            self.vel_x = -self.vel_x
            # Asegurar que no se salga del canvas
            self.x = max(self.radio, min(ancho - self.radio, self.x))
        
        if self.y - self.radio <= 0 or self.y + self.radio >= alto:
            self.vel_y = -self.vel_y
            # Asegurar que no se salga del canvas
            self.y = max(self.radio, min(alto - self.radio, self.y))
        
        # Actualizar posición en canvas
        self.canvas.coords(self.id, self.x - self.radio, self.y - self.radio,
                          self.x + self.radio, self.y + self.radio)
    
    def get_posicion(self):
        return (self.x, self.y, self.radio)

class Animacion:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Animación - Esferas Rebotes")
        self.ventana.geometry("800x600")
        
        # Variables de control
        self.animando = True
        self.velocidad = 10  # ms entre frames
        
        # Crear canvas
        self.canvas = tk.Canvas(self.ventana, width=780, height=500, bg='white')
        self.canvas.pack(pady=10)
        
        # Crear esferas
        self.crear_esferas()
        
        # Controles de velocidad
        frame_control = ttk.LabelFrame(self.ventana, text="Controles de Velocidad")
        frame_control.pack(pady=10, padx=20, fill='x')
        
        ttk.Label(frame_control, text="Velocidad:").pack(side='left', padx=5)
        
        self.escala_velocidad = ttk.Scale(frame_control, from_=1, to=30, 
                                         orient='horizontal', length=200,
                                         command=self.cambiar_velocidad)
        self.escala_velocidad.set(self.velocidad)
        self.escala_velocidad.pack(side='left', padx=5)
        
        self.label_velocidad = ttk.Label(frame_control, text=f"{self.velocidad} ms")
        self.label_velocidad.pack(side='left', padx=5)
        
        # Botones de control
        frame_botones = ttk.Frame(self.ventana)
        frame_botones.pack(pady=10)
        
        btn_pausa = ttk.Button(frame_botones, text="Pausa/Reanudar", 
                              command=self.toggle_animacion)
        btn_pausa.pack(side='left', padx=5)
        
        btn_reiniciar = ttk.Button(frame_botones, text="Reiniciar Posiciones", 
                                  command=self.reiniciar_posiciones)
        btn_reiniciar.pack(side='left', padx=5)
        
        btn_cerrar = ttk.Button(frame_botones, text="Cerrar", 
                               command=self.cerrar)
        btn_cerrar.pack(side='left', padx=5)
        
        # Iniciar animación
        self.animar()
    
    def crear_esferas(self):
        """Crea dos esferas con posiciones y velocidades aleatorias"""
        ancho = 780
        alto = 500
        
        # Esfera 1 (roja)
        radio1 = 30
        x1 = random.randint(radio1, ancho - radio1)
        y1 = random.randint(radio1, alto - radio1)
        vel_x1 = random.uniform(2, 5)
        vel_y1 = random.uniform(2, 5)
        
        # Esfera 2 (azul)
        radio2 = 30
        x2 = random.randint(radio2, ancho - radio2)
        y2 = random.randint(radio2, alto - radio2)
        vel_x2 = random.uniform(2, 5)
        vel_y2 = random.uniform(2, 5)
        
        self.esfera1 = Esfera(self.canvas, x1, y1, radio1, 'red', vel_x1, vel_y1)
        self.esfera2 = Esfera(self.canvas, x2, y2, radio2, 'blue', vel_x2, vel_y2)
    
    def verificar_colision(self):
        """Verifica si las esferas colisionan y actualiza velocidades"""
        x1, y1, r1 = self.esfera1.get_posicion()
        x2, y2, r2 = self.esfera2.get_posicion()
        
        # Calcular distancia entre centros
        distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        
        # Si hay colisión
        if distancia <= r1 + r2:
            # Calcular vector de colisión
            dx = x2 - x1
            dy = y2 - y1
            
            # Normalizar
            if distancia == 0:
                distancia = 0.001
            nx = dx / distancia
            ny = dy / distancia
            
            # Calcular velocidad relativa
            v1x, v1y = self.esfera1.vel_x, self.esfera1.vel_y
            v2x, v2y = self.esfera2.vel_x, self.esfera2.vel_y
            
            # Velocidad relativa en dirección de la normal
            v_rel = (v2x - v1x) * nx + (v2y - v1y) * ny
            
            # Si se están acercando
            if v_rel < 0:
                # Coeficiente de restitución (elasticidad)
                e = 0.8
                
                # Impulso
                impulso = (1 + e) * v_rel / 2
                
                # Actualizar velocidades
                self.esfera1.vel_x += impulso * nx
                self.esfera1.vel_y += impulso * ny
                self.esfera2.vel_x -= impulso * nx
                self.esfera2.vel_y -= impulso * ny
                
                # Separar las esferas para evitar que se peguen
                overlap = (r1 + r2) - distancia
                if overlap > 0:
                    separacion_x = nx * overlap / 2
                    separacion_y = ny * overlap / 2
                    self.esfera1.x -= separacion_x
                    self.esfera1.y -= separacion_y
                    self.esfera2.x += separacion_x
                    self.esfera2.y += separacion_y
    
    def animar(self):
        """Función principal de animación"""
        if self.animando:
            # Obtener dimensiones del canvas
            ancho = self.canvas.winfo_width()
            alto = self.canvas.winfo_height()
            
            if ancho > 1 and alto > 1:  # Verificar que el canvas esté visible
                # Mover esferas
                self.esfera1.mover(ancho, alto)
                self.esfera2.mover(ancho, alto)
                
                # Verificar colisión entre esferas
                self.verificar_colision()
            
            # Programar siguiente frame
            self.ventana.after(self.velocidad, self.animar)
    
    def cambiar_velocidad(self, valor):
        """Cambia la velocidad de animación"""
        self.velocidad = int(float(valor))
        self.label_velocidad.config(text=f"{self.velocidad} ms")
    
    def toggle_animacion(self):
        """Pausa o reanuda la animación"""
        self.animando = not self.animando
        if self.animando:
            self.animar()
    
    def reiniciar_posiciones(self):
        """Reinicia las posiciones de las esferas"""
        # Eliminar esferas actuales
        self.canvas.delete(self.esfera1.id)
        self.canvas.delete(self.esfera2.id)
        
        # Crear nuevas esferas
        self.crear_esferas()
    
    def cerrar(self):
        """Cierra la ventana de animación"""
        self.animando = False
        self.ventana.destroy()


class AplicacionPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Laboratorio Tkinter - Taller")
        self.root.geometry("400x300")
        self.root.configure(bg='#f0f0f0')
        
        # Control de ventanas abiertas
        self.ventanas_abiertas = []
        
        # Configurar estilo
        self.estilo = ttk.Style()
        self.estilo.configure('TButton', font=('Arial', 12), padding=10)
        
        # Título
        titulo = tk.Label(root, text="TALLER", 
                         font=('Arial', 20, 'bold'),
                         bg='#f0f0f0', fg='#333')
        titulo.pack(pady=20)
        
        # Botones del menú principal
        btn_analisis = ttk.Button(root, text="1. Análisis de Números", 
                                 command=self.abrir_analisis)
        btn_analisis.pack(pady=10, padx=20, fill='x')
        
        btn_ficha = ttk.Button(root, text="2. Ficha Personal", 
                              command=self.abrir_ficha)
        btn_ficha.pack(pady=10, padx=20, fill='x')
        
        btn_animacion = ttk.Button(root, text="3. Animación", 
                                  command=self.abrir_animacion)
        btn_animacion.pack(pady=10, padx=20, fill='x')
        
        btn_salir = ttk.Button(root, text="Salir", command=self.salir)
        btn_salir.pack(pady=20, padx=20, fill='x')
    
    def registrar_ventana(self, ventana_toplevl):
        """Registra una ventana y configura su cierre"""
        self.ventanas_abiertas.append(ventana_toplevl)
        
        # Configurar callback para cuando se cierre la ventana
        def on_closing():
            if ventana_toplevl in self.ventanas_abiertas:
                self.ventanas_abiertas.remove(ventana_toplevl)
            ventana_toplevl.destroy()
        
        ventana_toplevl.protocol("WM_DELETE_WINDOW", on_closing)
    
    def puede_abrir_ventana(self):
        """Verifica si se pueden abrir más ventanas (máximo 2)"""
        # Limpiar ventanas que ya no existen
        self.ventanas_abiertas = [v for v in self.ventanas_abiertas if v.winfo_exists()]
        
        if len(self.ventanas_abiertas) >= 2:
            messagebox.showwarning("Límite de Ventanas", "No puedes abrir más de 2 ventanas simultáneamente. Cierra una primero.")
            return False
        return True
    
    def abrir_analisis(self):
        if not self.puede_abrir_ventana():
            return
        ventana = tk.Toplevel(self.root)
        self.registrar_ventana(ventana)
        AnalisisNumeros(ventana)
    
    def abrir_ficha(self):
        if not self.puede_abrir_ventana():
            return
        ventana = tk.Toplevel(self.root)
        self.registrar_ventana(ventana)
        FichaPersonal(ventana)
    
    def abrir_animacion(self):
        if not self.puede_abrir_ventana():
            return
        ventana = tk.Toplevel(self.root)
        self.registrar_ventana(ventana)
        Animacion(ventana)
    
    def salir(self):
        if messagebox.askyesno("Salir", "¿Está seguro que desea salir?"):
            self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionPrincipal(root)
    root.mainloop()