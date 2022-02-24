from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Tkinter Tutorial")
root.iconbitmap("hazard.icns")

my_img1 = ImageTk.PhotoImage(Image.open("/Users/nicholasphandinata/Desktop/Python/tkinter/images/sasuke1.png"))
my_img2 = ImageTk.PhotoImage(Image.open("/Users/nicholasphandinata/Desktop/Python/tkinter/images/sasuke2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("/Users/nicholasphandinata/Desktop/Python/tkinter/images/sasuke3.png"))
my_img4 = ImageTk.PhotoImage(Image.open("/Users/nicholasphandinata/Desktop/Python/tkinter/images/naruto1.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("/Users/nicholasphandinata/Desktop/Python/tkinter/images/naruto2.jpg"))

img_list = [my_img1,my_img2,my_img3,my_img4,my_img5]

my_label = Label(image=my_img1)
status = Label(text="Image 1 of " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)

my_label.grid(row=0, column=0, columnspan=3)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def forward(img_num):
    global my_label
    global status
    global button_forward
    global button_back
    
    my_label.grid_forget()

    my_label = Label(image=img_list[img_num-1])
    status = Label(text="Image " + str(img_num) + " of " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)

    button_forward = Button(root, text=">>", command=lambda: forward(img_num+1))
    button_back = Button(root, text="<<", command=lambda: back(img_num-1))

    if img_num == 5:
        button_forward = Button(root, text=">>", state=DISABLED)
    
    my_label.grid(row=0, column=0, columnspan=3)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

def back(img_num):
    global my_label
    global status
    global button_forward
    global button_back

    my_label.grid_forget()

    my_label = Label(image=img_list[img_num-1])
    status = Label(text="Image " + str(img_num) + " of " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)

    button_forward = Button(root, text=">>", command=lambda: forward(img_num+1))
    button_back = Button(root, text="<<", command=lambda: back(img_num-1))

    if img_num == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


button_back = Button(root, text="<<", command=back, state=DISABLED)
button_quit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)


root.mainloop()