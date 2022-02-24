from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Tkinter Tutorial")
root.iconbitmap("hazard.icns")

""" r = IntVar()
r.set(2)

def clicked(value):
    myLabel1 = Label(root, text=value)
    myLabel1.pack()

Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

myLabel1 = Label(root, text=r.get())
myLabel1.pack()

button = Button(root, text="Click here", command=lambda: clicked(r.get()))
button.pack() """

modes = [
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Beef","Beef")
]

pizza = StringVar()
pizza.set("Beef")

for text, mode in modes:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

def clicked(value):
    myLabel1 = Label(root, text=value)
    myLabel1.pack()

button = Button(root, text="Click here", command=lambda: clicked(pizza.get()))
button.pack()

root.mainloop()