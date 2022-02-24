from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title("Tkinter Tutorial")
root.geometry("400x400")

def show():
    my_label = Label(root, text=var.get()).pack()
    my_label2 = Label(root, text=var2.get()).pack()

var = IntVar()
var2 = StringVar()

c = Checkbutton(root, text="Box 1", variable=var).pack()
c2 = Checkbutton(root, text="Box 2", variable=var2, onvalue="On", offvalue="Off")
c2.deselect()
c2.pack()

btn = Button(root, text="Display selection", command=show).pack()

root.mainloop()