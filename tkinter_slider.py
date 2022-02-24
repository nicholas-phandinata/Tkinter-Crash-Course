from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title("Tkinter Tutorial")
root.geometry("400x400")

def slide():
    #my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

vertical = Scale(root, from_=200, to=1000)
vertical.pack()

horizontal = Scale(root, from_=200, to=1000, orient=HORIZONTAL)
horizontal.pack()

my_label = Label(root, text=horizontal.get()).pack()

my_btn = Button(root, text="Slide info", command=slide).pack()

root.mainloop()