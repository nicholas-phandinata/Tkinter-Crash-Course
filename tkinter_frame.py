from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Tkinter Tutorial")
root.iconbitmap("hazard.icns")

frame = LabelFrame(root, text="This is a frame", padx=5, pady=5)
frame.pack(padx=15, pady=15)

button = Button(frame, text="Don't click here")
button2 = Button(frame, text="here too")

button.grid(row=0, column=0)
button2.grid(row=1, column=1)

root.mainloop()