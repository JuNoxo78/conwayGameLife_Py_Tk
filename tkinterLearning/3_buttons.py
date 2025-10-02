from tkinter import *

root = Tk()

def my_click():
    my_label = Label(root, text="Look I clicked a Button!")
    my_label.pack()

# myButton = Button(root, text="Click me!", command=my_click, fg="blue", bg="skyblue") # Así es como un botón es útil y con colores
# myButton = Button(root, text="Click me!", state="disabled") # Botón Deshabilitado
myButton = Button(root, text="Click me!", padx=50, pady=50) # Botón con tamaño modificado

myButton.pack()

root.mainloop()
