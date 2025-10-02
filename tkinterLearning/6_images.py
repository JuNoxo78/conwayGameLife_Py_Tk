from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.resizable(False, False)
root.title("Images Practice")
root.iconbitmap("icon.ico") # The icon of the window

button_quit = Button(root, text="Exit Program", command=root.quit) # Quit Button

img = Image.open("img/IMG_20200726_144749.jpg")

nuevo_ancho = 400

ancho_original, alto_original = img.size
nuevo_alto = int((nuevo_ancho / ancho_original) * alto_original)

resize_img = img.resize((nuevo_ancho, nuevo_alto), Image.LANCZOS)

my_img = ImageTk.PhotoImage(resize_img) # Step 1: Define image
my_label = Label(image=my_img) # Step 2: Put the image into another widget
my_label.pack() # Step 3: Put the widget in the window

button_quit.pack()

root.mainloop()