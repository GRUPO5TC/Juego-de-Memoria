Fernanda
import tkinter as tk
import random

class JuegoMemoria:
    def init(self, root):
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

*