from tkinter import *

root = Tk()

e = Entry(root, width=50, fg="blue", bg="skyblue", borderwidth=10) # tamaño, colores, ancho del borde
e.pack()
e.insert(0, "Ingrese su nombre") # Una forma de insertar texto (no un placeholder)

def my_click():
    hello_msg = "Hello " + e.get() # Con esto se consigue el texto
    my_label = Label(root, text=hello_msg)
    my_label.pack()

myButton = Button(root, text="Enter your name!", command=my_click, fg="blue", bg="skyblue")

myButton.pack()

root.mainloop()
