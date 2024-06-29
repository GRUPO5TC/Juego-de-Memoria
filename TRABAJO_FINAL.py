import tkinter as tk
import random

class JuegoMemoria:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Memoria con Autómata de Pila")
        
        self.secuencia = []
        self.secuencia_jugador = []
        self.nivel = 1
        self.tiempo_destello = 500
        
        self.info_label = tk.Label(root, text="Presiona 'Iniciar' para comenzar", font=('Helvetica', 16))
        self.info_label.pack(pady=20)
        
        self.start_button = tk.Button(root, text="Iniciar", command=self.iniciar_juego, font=('Helvetica', 14))
        self.start_button.pack(pady=10)
        
        self.button_frame = tk.Frame(root)
        self.button_frame.pack()
        
        self.buttons = {}
        self.colores = ["red", "green", "blue", "yellow"]
        self.extra_colores = ["purple", "orange", "pink", "brown"]
        for color in self.colores:
            button = tk.Button(self.button_frame, bg=color, width=10, height=5, state='disabled', command=lambda c=color: self.eleccion_jugador(c))
relief='raised', font=('Helvetica', 12, 'bold'))            
            button.pack(side='left', padx=15, pady=15)
            self.buttons[color] = button

        self.center_frame = tk.Frame(root)
        self.center_frame.pack(side='right', padx=20, pady=20, expand=True)

        self.pila_frame = tk.Frame(self.center_frame)
        self.pila_frame.pack(pady=10)
        self.pila_label = tk.Label(self.pila_frame, text="Pila", font=('Helvetica', 16))
        self.pila_label.pack(pady=10)
        self.pila_text = tk.Text(self.pila_frame, height=10, width=15, font=('Helvetica', 14), bg="white", relief='sunken', bd=2)
        self.pila_text.pack()

    def iniciar_juego(self):
        self.secuencia = []
        self.secuencia_jugador = []
        self.nivel = 1
        self.tiempo_destello = 500
        self.actualizar_pila(inicial=True)
        self.info_label.config(text="Memoriza la secuencia")
        self.root.after(1000, self.siguiente_nivel)
        
    def siguiente_nivel(self):
        self.info_label.config(text=f"Nivel {self.nivel}")
        nuevo_color = random.choice(self.colores)
        self.secuencia.append(nuevo_color)
        if self.nivel % 3 == 0 and self.extra_colores:
            color_agregar = self.extra_colores.pop()
            self.colores.append(color_agregar)
            button = tk.Button(self.button_frame, bg=color_agregar, width=10, height=5, state='disabled', command=lambda c=color_agregar:
   self.eleccion_jugador(c), relief='raised', font=('Helvetica', 12, 'bold'))                            
            button.pack(side='left', padx=15, pady=15)
            self.buttons[color_agregar] = button
        if self.nivel % 2 == 0 and self.tiempo_destello >200:
            self.tiempo_destello -= 50
        self.actualizar_pila(inicial=True)
        self.mostrar_secuencia(0)
        
    def mostrar_secuencia(self, indice):
        if indice < len(self.secuencia):
            color = self.secuencia[indice]
            self.destello_boton(color)
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

    def habilitar_botones(self):
        for button in self.buttons.values():
            button.config(state='normal')

    def deshabilitar_botones(self):
        for button in self.buttons.values():
            button.config(state='disabled')

    def eleccion_jugador(self, color):
        self.secuencia_jugador.append(color)
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
            if self.secuencia_jugador[i] !=self.secuencia[-(i+1)]: #Comparar con la secuencia en ordeninverso
                return False
        return True

    def actualizar_pila(self, inicial):
        self.pila_text.delete('1.0', tk,END)
        if inicial:
            for _ in self.secuencia:
                self.pila_text.insert(tk.END, "???\n")
        else:
            for i in range(len(self.secuencia)):
                if i < len(self.secuencia_jugador):
                    self.pila_text.insert(tk,END, f"{self.secuencia[-(i+1)\n" #Mostrar en orden inverso
                else:
                      self.pila_text.insert(tk,END, "???\n")                    

root = tk.Tk()
juego = JuegoMemoria(root)
root.mainloop()
