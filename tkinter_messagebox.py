from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title("Tkinter Tutorial")
root.iconbitmap("hazard.icns")

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    #messagebox.showinfo("This is a popup", "Popup")
    #messagebox.showwarning("This is a popup", "Popup")
    response = messagebox.askquestion("This is a popup", "Popup")
    Label(root, text=response).pack()
"""     if response == 1:
        Label(root, text="Yes").pack()
    else:
        Label(root, text="No").pack() """

Button(root, text="Click here", command=popup).pack()

root.mainloop()