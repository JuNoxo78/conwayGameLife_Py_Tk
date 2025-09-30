import tkinter as tk
import numpy as np
import gameRules as gR

root = tk.Tk()
root.title("Conway Life Game")
root.iconbitmap("icon.ico")
root.configure(bg="#ffffce")
root.resizable(False, False)

ancho_ventana = 1034
alto_ventana = 676

# Centrar ventana
ancho_pantalla = root.winfo_screenwidth()
alto_pantalla = root.winfo_screenheight() - 77

x = (ancho_pantalla // 2) - (ancho_ventana // 2)
y = (alto_pantalla // 2) - (alto_ventana // 2)

root.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

# UI atributos
TAM_CUADRO = 20
FILAS = gR.FILAS
COLUMNAS = gR.COLUMNAS
DEACTIVE_COLOR = "#303030"
ACTIVE_COLOR = "#FFFFFF"
OUTLINE_COLOR = "#707070"

# Funciones para crear células con el mouse
can_change_action = True
color_action = ACTIVE_COLOR

def cambiar_color(event):
    # event.widget es el canvas, event.x y event.y son las coordenadas del clic
    item = canvas.find_closest(event.x, event.y)

    global color_action
    global can_change_action

    if canvas.itemcget(item, "fill") == DEACTIVE_COLOR and can_change_action:
        color_action = ACTIVE_COLOR
        can_change_action = False

    if canvas.itemcget(item, "fill") == ACTIVE_COLOR and can_change_action:
        color_action = DEACTIVE_COLOR
        can_change_action = False

    canvas.itemconfig(item, fill=color_action)

mouse_pressed = False

def on_press(event):
    global mouse_pressed
    mouse_pressed = True
    cambiar_color(event)

def on_release(event):
    global mouse_pressed
    global can_change_action
    mouse_pressed = False
    can_change_action = True

def on_motion(event):
    if mouse_pressed:
        cambiar_color(event)

# Función para obtener matriz de canvas
def generate_universe_array():
    def rect_to_val(rect):
        return 1 if canvas.itemcget(rect, "fill") == ACTIVE_COLOR else 0
    vfunc = np.vectorize(rect_to_val)
    return vfunc(rect_ids)

# Función para obtener próxima generación
def paint_next_generation():
    actual_generation = generate_universe_array()
    if not np.array_equal(actual_generation, np.array(gR.historia)[gR.index_iteration]):
        gR.historia = gR.historia[:gR.index_iteration + 1]
        gR.historia.append(actual_generation)
        gR.index_iteration += 1

    next_generation = gR.siguiente_generacion(actual_generation)

    color_next_generation = np.where(next_generation == 1, ACTIVE_COLOR, DEACTIVE_COLOR)

    # def coloring(rect, color):
    #     canvas.itemconfig(rect, fill=color)
    # vfunc = np.vectorize(coloring)
    # vfunc(rect_ids, color_next_generation)

    for rect, color in zip(rect_ids.ravel(), color_next_generation.ravel()):
        canvas.itemconfig(rect, fill=color)

# Función para obtener generación previa
def paint_prev_generation():
    prev_generation = gR.anterior_generacion()
    color_prev_generation = np.where(prev_generation == 1, ACTIVE_COLOR, DEACTIVE_COLOR)

    for rect, color in zip(rect_ids.ravel(), color_prev_generation.ravel()):
        canvas.itemconfig(rect, fill=color)

# Siguiente generación con barra espaciadora
press = [False]

def space_next_gen():
    if press[0]:
        paint_next_generation()
        root.after(100, space_next_gen)

def on_space_press(event):
    if not press[0]:
        press[0] = True
        space_next_gen()

def on_space_release(event):
    press[0] = False

root.bind("<KeyPress-space>", on_space_press)
root.bind("<KeyRelease-space>", on_space_release)

# Función para limpiar canvas
def clean_canvas():
    gR.historia = [np.zeros((FILAS, COLUMNAS), dtype=int)]
    gR.index_iteration = 0
    for item in canvas.find_all():
        canvas.itemconfig(item, fill=DEACTIVE_COLOR)

# Canvas Widget para el juego
canvas = tk.Canvas(root, width=TAM_CUADRO * COLUMNAS, height=TAM_CUADRO * FILAS)

# Generación de universo vacío
rect_ids=np.empty((FILAS, COLUMNAS), dtype=object)
for fila in range(FILAS):
    for col in range(COLUMNAS):
        x1 = col * TAM_CUADRO
        y1 = fila * TAM_CUADRO
        x2 = x1 + TAM_CUADRO
        y2 = y1 + TAM_CUADRO
        rect = canvas.create_rectangle(
            x1, y1, x2, y2,
            fill=DEACTIVE_COLOR,
            outline=OUTLINE_COLOR,
            width=1
        )
        rect_ids[fila, col] = rect

        # Eventos de click y hover
        canvas.tag_bind(rect, "<Button-1>", cambiar_color)
        canvas.tag_bind(rect, "<ButtonPress-1>", on_press)
        canvas.tag_bind(rect, "<ButtonRelease-1>", on_release)
        canvas.tag_bind(rect, "<B1-Motion>", on_motion)

# Botones de Control
button_prevGeneration = tk.Button(root, text="Previous Generation", command=paint_prev_generation)
button_nextGeneration = tk.Button(root, text="Next Generation", command=paint_next_generation)
button_clear = tk.Button(root, text="Clear Uhiverse", command=clean_canvas)

# Posicionando widgets en ventana
canvas.grid(row=1, column=0, columnspan=3, padx=15, pady=15)
button_prevGeneration.grid(row=0, column=0, pady=(15, 0))
button_nextGeneration.grid(row=0, column=1, pady=(15, 0))
button_clear.grid(row=0, column=2, pady=(15, 0))

root.focus_set()
root.mainloop()