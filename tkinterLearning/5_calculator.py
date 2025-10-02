import tkinter.font
from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.resizable(False, False)
default_font = tkinter.font.nametofont("TkDefaultFont")
default_font.configure(family="Courier New", size=11, weight="bold")

e = Entry(root, width=40, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=5, pady=10)  # Con columnspan indicamos que el elemento ocupe tres columnas
# Los padx y pady, indican espaciado interno, entre la celda del grid y los elementos que contiene

def button_click(number):
    e.insert(END, number)

def button_clear():
    e.delete(0, END)

def new_num():
    first_number = e.get()
    global f_num
    f_num = float(first_number)
    e.delete(0, END)

def button_add():
    new_num()
    global operation
    operation = "a"

def button_substract():
    new_num()
    global operation
    operation = "s"
    return

def button_multiply():
    new_num()
    global operation
    operation = "m"
    return

def button_divide():
    new_num()
    global operation
    operation = "d"
    return

def button_equal():
    second_number = e.get()
    e.delete(0, END)

    result = 0.0

    if operation == "a":
        result = f_num + float(second_number)

    if operation == "s":
        result = f_num - float(second_number)

    if operation == "m":
        result = f_num * float(second_number)

    if operation == "d":
        result = f_num / float(second_number)

    e.insert(0, str(result))

# Define buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

buttonEqual = Button(root, text="=", pady=20, command=button_equal)
buttonClear = Button(root, text="Clear", pady=20, command=button_clear)

buttonAdd = Button(root, text="+", padx=40, pady=20, command=button_add)
buttonSubstract = Button(root, text="-", padx=40, pady=20, command=button_substract)
buttonMultiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
buttonDivide = Button(root, text="/", padx=40, pady=20, command=button_divide)

# Put the buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
buttonAdd.grid(row=4, column=1)
buttonSubstract.grid(row=4, column=2)

buttonClear.grid(row=5, column=0, sticky="ew")
buttonMultiply.grid(row=5, column=1)
buttonDivide.grid(row=5, column=2)

buttonEqual.grid(row=6, column=0, columnspan=3, sticky="ew")

root.mainloop()