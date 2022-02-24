from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title("Tkinter Tutorial")
root.iconbitmap("hazard.icns")
my_img1 = None
my_img2 = None

def open(value):
    if value == 1:
        global my_img1
        window2 = Toplevel()
        window2.title("Second window")
        my_img1 = ImageTk.PhotoImage(Image.open("/Users/nicholasphandinata/Desktop/Python/tkinter/images/naruto1.jpg"))
        my_label = Label(window2, image=my_img1)
        my_label.pack()
        btn3 = Button(window2, text="Close second window", command=window2.destroy)
        btn3.pack()
    
    else:
        global my_img2
        window3 = Toplevel()
        window3.title("Third window")
        my_img2 = ImageTk.PhotoImage(Image.open("/Users/nicholasphandinata/Desktop/Python/tkinter/images/sasuke1.png"))
        my_label = Label(window3, image=my_img2)
        my_label.pack()
        btn3 = Button(window3, text="Close third window", command=window3.destroy)
        btn3.pack()

btn = Button(root, text="Open second window here", command=lambda: open(1))
btn.pack()
btn2 = Button(root, text="Open third window here", command=lambda: open(2))
btn2.pack()

root.mainloop()