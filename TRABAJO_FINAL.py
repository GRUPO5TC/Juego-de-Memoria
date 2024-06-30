import tkinter as tk
import random

class JuegoMemoria:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Memoria con Autómata de Pila")
        self.root.geometry("700x400")
        
        self.modo_juego = None  # Para almacenar el modo de juego seleccionado
        self.secuencia = []
        self.secuencia_jugador = []
        self.nivel = 1
        self.tiempo_destello = 500
        
        # Menú Inicial
        self.menu_frame = tk.Frame(root)
        self.menu_frame.pack(pady=20)
        self.menu_label = tk.Label(self.menu_frame, text="Seleccione el modo de juego", font=('Helvetica', 16))
        self.menu_label.pack(pady=10)
        self.clasico_button = tk.Button(self.menu_frame, text="Modo Clásico", command=self.modo_clasico, font=('Helvetica', 14), bg="lightgreen")
        self.clasico_button.pack(pady=5)
        self.patrones_button = tk.Button(self.menu_frame, text="Modo Patrones Complejos", command=self.modo_patrones, font=('Helvetica', 14), bg="lightblue")
        self.patrones_button.pack(pady=5)

        # Inicializar widgets del juego, ocultos inicialmente
        self.info_label = tk.Label(root, text="", font=('Helvetica', 16), bg="lightblue")
        self.start_button = tk.Button(root, text="Iniciar", command=self.iniciar_juego, font=('Helvetica', 14), bg="lightgreen")
        self.button_frame = tk.Frame(root, bg="lightgrey")
        self.buttons = {}
        self.colores = ["red", "green", "blue", "yellow"]
        self.extra_colores = ["purple", "orange", "pink", "brown"]
        for color in self.colores:
            button = tk.Button(self.button_frame, bg=color, width=10, height=5, state='disabled', command=lambda c=color: self.eleccion_jugador(c), relief='raised', font=('Helvetica', 12, 'bold'))
            button.pack(side='left', padx=15, pady=15)
            self.buttons[color] = button
            button.pack_forget()  # Ocultar botones al inicio

        self.figuras = ["cuadrado", "circulo", "triangulo", "rombo"]
        self.figuras_buttons = {}
        for figura in self.figuras:
            button = tk.Button(self.button_frame, text=figura.capitalize(), width=10, height=5, state='disabled', command=lambda f=figura: self.eleccion_jugador(f), relief='raised', font=('Helvetica', 12, 'bold'))
            button.pack(side='left', padx=15, pady=15)
            self.figuras_buttons[figura] = button
            button.pack_forget()  # Ocultar botones al inicio

        self.center_frame = tk.Frame(root, bg="lightblue")
        self.pila_frame = tk.Frame(self.center_frame, bg="lightblue")
        self.pila_label = tk.Label(self.pila_frame, text="Pila", font=('Helvetica', 16), bg="lightblue")
        self.pila_listbox = tk.Listbox(self.pila_frame, height=10, width=15, font=('Helvetica', 14), bg="white", relief='sunken', bd=2)

        self.canvas = tk.Canvas(self.center_frame, width=200, height=200, bg="lightblue")
        self.canvas.pack(pady=20)
        self.canvas.pack_forget()  # Ocultar canvas al inicio

    def modo_clasico(self):
        self.modo_juego = "clasico"
        self.mostrar_botones(self.buttons)
        self.ocultar_botones(self.figuras_buttons)
        self.canvas.pack_forget()  # Ocultar canvas en modo clásico
        self.iniciar_juego()

    def modo_patrones(self):
        self.modo_juego = "patrones"
        self.mostrar_botones(self.figuras_buttons)
        self.ocultar_botones(self.buttons)
        self.canvas.pack(pady=20)  # Mostrar canvas en modo patrones
        self.iniciar_juego()

    def mostrar_botones(self, botones):
        for button in botones.values():
            button.pack(side='left', padx=15, pady=15)

    def ocultar_botones(self, botones):
        for button in botones.values():
            button.pack_forget()

    def iniciar_juego(self):
        self.menu_frame.pack_forget()  # Ocultar menú inicial
        self.secuencia = []
        self.secuencia_jugador = []
        self.nivel = 1
        self.tiempo_destello = 500

        # Mostrar widgets del juego
        self.info_label.pack(pady=20, fill=tk.X)
        self.start_button.pack(pady=10)
        self.button_frame.pack(pady=20)
        self.center_frame.pack(side='right', padx=20, pady=20, expand=True)
        self.pila_frame.pack(pady=10)
        self.pila_label.pack(pady=10)
        self.pila_listbox.pack()
        
        self.actualizar_pila(inicial=True)
        self.info_label.config(text="Memoriza la secuencia")
        self.root.after(1000, self.siguiente_nivel)
        
    def siguiente_nivel(self):
        self.info_label.config(text=f"Nivel {self.nivel}")
        if self.modo_juego == "clasico":
            nuevo_color = random.choice(self.colores)
            self.secuencia.append(nuevo_color)
            if self.nivel % 3 == 0 and self.extra_colores:
                color_agregar = self.extra_colores.pop()
                self.colores.append(color_agregar)
                button = tk.Button(self.button_frame, bg=color_agregar, width=10, height=5, state='disabled', command=lambda c=color_agregar: self.eleccion_jugador(c), relief='raised', font=('Helvetica', 12, 'bold'))
                button.pack(side='left', padx=15, pady=15)
                self.buttons[color_agregar] = button
            if self.nivel % 2 == 0 and self.tiempo_destello > 200:
                self.tiempo_destello -= 50
            self.actualizar_pila(inicial=True)
            self.mostrar_secuencia(0)
        elif self.modo_juego == "patrones":
            nuevo_item = random.choice(self.figuras)
        
        self.secuencia.append(nuevo_item)
        
        if self.nivel % 2 == 0 and self.tiempo_destello > 200:
            self.tiempo_destello -= 50
        
        self.actualizar_pila(inicial=True)
        self.mostrar_secuencia(0)
        
    def mostrar_secuencia(self, indice):
        if indice < len(self.secuencia):
            item = self.secuencia[indice]
            if self.modo_juego == "clasico":
                self.destello_boton(item)
            elif self.modo_juego == "patrones":
                self.mostrar_figura(item)
            self.root.after(self.tiempo_destello * 2, lambda: self.mostrar_secuencia(indice + 1))
        else:
            self.habilitar_botones()
            self.info_label.config(text="Reproduce la secuencia en orden inverso")
        
    def destello_boton(self, color):
        button = self.buttons[color]
        color_original = button.cget('bg')
        button.config(state='normal', bg='white', relief='raised')
        self.root.after(self.tiempo_destello, lambda: self.restablecer_boton(button, color_original))
        
    def restablecer_boton(self, button, color_original):
        button.config(state='disabled', bg=color_original, relief='sunken')

    def mostrar_figura(self, figura):
        self.canvas.delete("all")
        if figura == "cuadrado":
            self.canvas.create_rectangle(50, 50, 150, 150, fill="black")
        elif figura == "circulo":
            self.canvas.create_oval(50, 50, 150, 150, fill="black")
        elif figura == "triangulo":
            self.canvas.create_polygon(50, 150, 150, 150, 100, 50, fill="black")
        elif figura == "rombo":
            self.canvas.create_polygon(100, 50, 150, 100, 100, 150, 50, 100, fill="black")
        self.root.after(self.tiempo_destello, self.canvas.delete, "all")
                
    def habilitar_botones(self):
        if self.modo_juego == "clasico":
            for button in self.buttons.values():
                button.config(state='normal')
        elif self.modo_juego == "patrones":
            for button in self.figuras_buttons.values():
                button.config(state='normal')
        
    def deshabilitar_botones(self):
        for button in self.buttons.values():
            button.config(state='disabled')
        for button in self.figuras_buttons.values():
            button.config(state='disabled')
        
    def eleccion_jugador(self, item):
        self.secuencia_jugador.append(item)
        if not self.verificar_secuencia():
            self.info_label.config(text="¡Secuencia incorrecta! Juego terminado.")
            self.deshabilitar_botones()
            return
        self.actualizar_pila(inicial=False)
        if len(self.secuencia_jugador) == len(self.secuencia):
            self.nivel += 1
            self.secuencia_jugador = []
            self.info_label.config(text="¡Correcto! Siguiente nivel")
            self.deshabilitar_botones()
            self.root.after(1000, self.siguiente_nivel)

    def verificar_secuencia(self):
        for i in range(len(self.secuencia_jugador)):
            if self.secuencia_jugador[i] != self.secuencia[-(i+1)]:  # Comparar con la secuencia en orden inverso
                return False
        return True

    def actualizar_pila(self, inicial):
        self.pila_listbox.delete(0, tk.END)
        if inicial:
            for _ in self.secuencia:
                self.pila_listbox.insert(tk.END, "???")
        else:
            for i in range(len(self.secuencia)):
                if i < len(self.secuencia_jugador):
                    self.pila_listbox.insert(tk.END, self.secuencia[-(i+1)])  # Mostrar en orden inverso
                else:
                    self.pila_listbox.insert(tk.END, "???")

root = tk.Tk()
juego = JuegoMemoria(root)
root.mainloop()
root.mainloop()
