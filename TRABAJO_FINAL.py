import tkinter as tk
import random

class JuegoMemoria:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Memoria con Autómata de Pila")
        
        self.secuencia = []
        self.secuencia_jugador = []
        self.nivel = 1
        
        self.info_label = tk.Label(root, text="Presiona 'Iniciar' para comenzar", font=('Helvetica', 16))
        self.info_label.pack(pady=20)
        
        self.start_button = tk.Button(root, text="Iniciar", command=self.iniciar_juego, font=('Helvetica', 14))
        self.start_button.pack(pady=10)
        
        self.button_frame = tk.Frame(root)
        self.button_frame.pack()
        
        self.buttons = {}
        self.colores = ["red", "green", "blue", "yellow"]
        for color in self.colores:
            button = tk.Button(self.button_frame, bg=color, width=10, height=5, state='disabled', command=lambda c=color: self.eleccion_jugador(c))
            button.pack(side='left', padx=10)
            self.buttons[color] = button
        
    def iniciar_juego(self):
        self.secuencia = []
        self.secuencia_jugador = []
        self.nivel = 1
        self.info_label.config(text="Memoriza la secuencia")
        self.root.after(1000, self.siguiente_nivel)
        
    def siguiente_nivel(self):
        self.info_label.config(text=f"Nivel {self.nivel}")
        self.secuencia.append(random.choice(self.colores))
        self.mostrar_secuencia(0)
        
    def mostrar_secuencia(self, indice):
        if indice < len(self.secuencia):
            color = self.secuencia[indice]
            self.destello_boton(color)
            self.root.after(1000, lambda: self.mostrar_secuencia(indice + 1))
        else:
            self.habilitar_botones()
            self.info_label.config(text="Reproduce la secuencia")
        
    def destello_boton(self, color):
        button = self.buttons[color]
        color_original = button.cget('bg')
        button.config(state='normal', bg='white', relief='raised')
        self.root.after(500, lambda: self.restablecer_boton(button, color_original))
        
    def restablecer_boton(self, button, color_original):
        button.config(state='disabled', bg=color_original, relief='sunken')
                

root = tk.Tk()
juego = JuegoMemoria(root)
root.mainloop()