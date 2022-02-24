from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Tkinter Tutorial")
root.iconbitmap("hazard.icns")

my_img = ImageTk.PhotoImage(Image.open("images/sasuke.png"))
my_label = Label(image=my_img)

button_quit = Button(root, text="Exit Program", command=root.quit)

my_label.pack()
button_quit.pack()

root.mainloop()