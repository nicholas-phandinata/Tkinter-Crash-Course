from tkinter import *

root = Tk()

""" myLabel = Label(root, text="Hello Nicz")

myLabel.pack()

root.mainloop() """

""" def myClick():
    myLabelClick = Label(root, text="Clicked !")
    myLabelClick.pack()

myLabel1 = Label(root, text="Hello Nicz")
myLabel2 = Label(root, text="Welcome")
#myButton = Button(root, text="Click here!", state=DISABLED)
myButton = Button(root, text="Click here!", padx=50, pady=50, command=myClick, fg="blue")

#myLabel1.grid(row=0, column=0)
#myLabel2.grid(row=1, column=0)
#myButton.grid(row=2, column=5)

myLabel1.pack()
myLabel2.pack()
myButton.pack() """

en = Entry(root, width=50, borderwidth=5, fg="red", bg="yellow")
en.pack()
en.insert(0, "Enter text here")

def myClick():
    myString = "Text: " + en.get()
    myLabelClick = Label(root, text=myString)
    myLabelClick.pack()

myLabel1 = Label(root, text="Hello Nicz")
myLabel2 = Label(root, text="Welcome")
#myButton = Button(root, text="Click here!", state=DISABLED)
myButton = Button(root, text="Submit!", padx=50, pady=50, command=myClick, fg="blue")

#myLabel1.grid(row=0, column=0)
#myLabel2.grid(row=1, column=0)
#myButton.grid(row=2, column=5)

myLabel1.pack()
myLabel2.pack()
myButton.pack() 

root.mainloop()