from tkinter import *

root = Tk()

myLabel_1 = Label(root, text="Hello World!")
myLabel_2 = Label(root, text="My name is Juan Lopez")

# Colocar los widgets en la cuadrícula
myLabel_1.grid(row=0, column=0)
myLabel_2.grid(row=1, column=5)

root.mainloop()