from tkinter import *

root = Tk()

# Step 01: Creating a Label Widget
myLabel = Label(root, text="Hello World!")

# Step 02: Shoving it onto the screen
myLabel.pack()

root.mainloop()  # Con esto, la interfaz se puede ver tanto como queramos, al establecerse en un bucle constante.
