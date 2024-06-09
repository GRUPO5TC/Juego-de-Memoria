import tkinter as tk
import random

class JuegoMemoria:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Memoria con Autómata de Pila")
        
        self.secuencia = []
        self.secuencia_jugador = []
        self.nivel = 1
        self.tiempo_destello = 1000
        
        self.info_label = tk.Label(root, text="Presiona 'Iniciar' para comenzar", font=('Helvetica', 16))
        self.info_label.pack(pady=20)
        
        self.start_button = tk.Button(root, text="Iniciar", command=self.iniciar_juego, font=('Helvetica', 14))
        self.start_button.pack(pady=10)
        
        self.button_frame = tk.Frame(root)
        self.button_frame.pack()
        
        self.buttons = {}
        self.colores = ["red", "green", "blue", "yellow", "purple", "orange", "pink", "cyan"]
        self.colores_disponibles = self.colores[:4]
        
        for color in self.colores_disponibles:
            button = tk.Button(self.button_frame, bg=color, width=10, height=5, state='disabled', command=lambda c=color: self.eleccion_jugador(c))
            button.pack(side='left', padx=10)
            self.buttons[color] = button
        
    def iniciar_juego(self):
        self.secuencia = []
        self.secuencia_jugador = []
        self.nivel = 1
        self.tiempo_destello = 1000
        self.info_label.config(text="Memoriza la secuencia")
        self.root.after(1000, self.siguiente_nivel)
        
    def siguiente_nivel(self):
        self.info_label.config(text=f"Nivel {self.nivel}")
        if self.nivel >= 3 and (self.nivel - 3) % 2 == 0 and len(self.colores_disponibles) < len(self.colores):
            self.colores_disponibles.append(self.colores[len(self.colores_disponibles)])
            nuevo_color = self.colores_disponibles[-1]
            button = tk.Button(self.button_frame, bg=nuevo_color, width=10, height=5, command=lambda c=nuevo_color: self.eleccion_jugador(c))
            button.pack(side='left', padx=10)
            self.buttons[nuevo_color] = button
        
        self.secuencia.append(random.choice(self.colores_disponibles))
        self.secuencia_jugador = []
        self.mostrar_secuencia(0)
        
    def mostrar_secuencia(self, indice):
        if indice < len(self.secuencia):
            color = self.secuencia[indice]
            self.destello_boton(color)
            self.root.after(self.tiempo_destello, lambda: self.mostrar_secuencia(indice + 1))
        else:
            self.habilitar_botones()
            self.info_label.config(text="Reproduce la secuencia al revés")
        
    def destello_boton(self, color):
        button = self.buttons[color]
        color_original = button.cget('bg')
        button.config(bg='white', relief='raised')
        self.root.after(500, lambda: self.restablecer_boton(button, color_original))
        
    def restablecer_boton(self, button, color_original):
        button.config(bg=color_original, relief='sunken')

    def habilitar_botones(self):
        for button in self.buttons.values():
            button.config(state='normal')

    def deshabilitar_botones(self):
        for button in self.buttons.values():
            button.config(state='disabled')

    def eleccion_jugador(self, color):
        self.secuencia_jugador.append(color)
        self.destello_boton(color)
        if self.secuencia_jugador == self.secuencia[::-1][:len(self.secuencia_jugador)]:
            if len(self.secuencia_jugador) == len(self.secuencia):
                self.nivel += 1
                if self.tiempo_destello > 300:
                    self.tiempo_destello -= 50
                self.info_label.config(text="¡Excelente! Memoriza la siguiente")
                self.deshabilitar_botones()
                self.root.after(1000, self.siguiente_nivel)
        else:
            self.info_label.config(text="¡ERROR! Juego terminado.")
            self.deshabilitar_botones()

root = tk.Tk()
juego = JuegoMemoria(root)
root.mainloop()