from tkinter import *
import tensorflow as tf 
import pandas as pd
import numpy as np

root = Tk()

classes = pd.read_csv('/Users/nicholasphandinata/Desktop/Python/tkinter/classes.csv')
model = tf.keras.models.load_model('/Users/nicholasphandinata/Desktop/Python/tkinter/model_timepredict2_complete_3kbatch_1.h5')

en1 = Entry(root, width=50, borderwidth=5, fg="red", bg="yellow")
en1.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
en1.insert(0, "Masukan waktu(12:00):")

en2 = Entry(root, width=75, borderwidth=5, fg="blue", bg="white")
en2.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

def myClick_Submit():
    user_input = en1.get()
    test_data = np.array([int(x) for x in user_input.split(':')])
    hour = float(test_data[0] / 23)
    minute = float(test_data[1] / 59)
    conv_data = np.array([hour,minute])
    pred = model.predict(conv_data.reshape(1,2), batch_size=1)
    top5 = np.argsort(pred[0])[:-6 :-1]
    pred_string = str(classes['Classes'][top5[0]]) + ", " + str(classes['Classes'][top5[1]]) + ", " + str(classes['Classes'][top5[2]]) + ", " + str(classes['Classes'][top5[3]]) + ", " + str(classes['Classes'][top5[4]])
    en2.insert(0, pred_string)

def myClick_Clear():
    en2.delete(0, END)

myButton_Submit = Button(root, text="Predict!", padx=25, pady=15, command=myClick_Submit, fg="blue")
myButton_Clear = Button(root, text="Clear!", padx=25, pady=15, command=myClick_Clear, fg="blue")

myButton_Submit.grid(row=2, column=0) 
myButton_Clear.grid(row=2, column=1) 

root.mainloop()