from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Images Practice")
root.iconbitmap("icon.ico")

img_1 = Image.open("img/1.jpg")
img_2 = Image.open("img/2.jpg")
img_3 = Image.open("img/3.jpg")
img_4 = Image.open("img/4.jpg")
img_5 = Image.open("img/5.jpg")
img_6 = Image.open("img/6.jpg")

img_list = [img_1, img_2, img_3, img_4, img_5, img_6]

nuevo_ancho = 300

resize_img_list = []

for img in img_list:
    ancho_original, alto_original = img.size
    nuevo_alto = int((nuevo_ancho / ancho_original) * alto_original)
    resize_img = ImageTk.PhotoImage(img.resize((nuevo_ancho, nuevo_alto)))
    resize_img_list.append(resize_img)

index_img = 0
my_label = Label(image=resize_img_list[index_img])
my_label.grid(row=0, column=0, columnspan=3)


def forward():
    global index_img
    global my_label

    if index_img < len(resize_img_list) - 1:
        button_back.configure(state="normal")
        index_img += 1
        if index_img == len(resize_img_list) - 1:
            button_forward.configure(state="disabled")
        my_label.grid_forget()
        my_label = Label(image=resize_img_list[index_img])
        my_label.grid(row=0, column=0, columnspan=3)

def back():
    global index_img
    global my_label

    if index_img > 0:
        button_forward.configure(state="normal")
        index_img -= 1
        if index_img == 0:
            button_back.configure(state="disabled")
        my_label.grid_forget()
        my_label = Label(image=resize_img_list[index_img])
        my_label.grid(row=0, column=0, columnspan=3)

button_back = Button(root, text="<<", command=back, state="disabled")
button_exit = Button(root, text="EXIT PROGRAM", command=root.quit)
button_forward = Button(root, text=">>", command=forward)

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()