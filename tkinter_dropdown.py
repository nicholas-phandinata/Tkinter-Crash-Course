from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title("Tkinter Tutorial")
root.geometry("400x400")

def show():
    my_label = Label(root, text=clicked.get()).pack()

opt = [
    "Attack Titan", 
    "War Hammer Titan", 
    "Armoured Titan", 
    "Cart Titan", 
    "Colossal Titan", 
    "Female Titan", 
    "Jaw Titan"
]

clicked = StringVar()
clicked.set("Attack Titan")

#menu = OptionMenu(root, clicked, "Attack Titan", "War Hammer Titan", "Armoured Titan", "Cart Titan", "Colossal Titan", "Female Titan", "Jaw Titan")
menu = OptionMenu(root, clicked, *opt)
menu.pack()

btn = Button(root, text="Display selection", command=show).pack()

root.mainloop()