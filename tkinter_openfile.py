from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title("Tkinter Tutorial")
root.iconbitmap("hazard.icns")

""" root.filename = filedialog.askopenfilename(initialdir="/Users/nicholasphandinata/Desktop/Python", title="Select a file", filetypes=(("png files", "*.png"), ("all files", "*.*")))
my_label = Label(root, text=root.filename).pack()
my_image = ImageTk.PhotoImage(Image.open(root.filename))
my_image_label = Label(image=my_image).pack() """
my_image = None

def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="/Users/nicholasphandinata/Desktop/Python", title="Select a file", filetypes=(("png files", "*.png"), ("all files", "*.*")))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()

btn = Button(root, text="Open a file", command=open).pack()

root.mainloop()