from tkinter import *

from tkinter import messagebox


# Create the window
mywindow = Tk() # Tk is classs

# Run the loop

# Entry Widgets

num1 = Entry(mywindow)
num2 = Entry(mywindow)
num1.grid(row=0,column=1)
num2.grid(row=1,column=1)

# Label Widgets
l1 = Label(mywindow,text="Enter Num 1:")
l1.grid(row=0,column=0)

Label(mywindow,text="Enter Num 2:").grid(row=1)

def closeWindow():
    mywindow.destroy()

def calculateSum():
    #print(float(num1.get()) + float(num2.get()))
    result = float(num1.get()) + float(num2.get())
    Label(mywindow,text="The Sum is {} ".format(result)).grid(row=10)
    messagebox.showinfo("The Sum is ",result)

Button(mywindow,text="Exit",command=closeWindow).grid(row=5)
Button(mywindow,text="Sum",command=calculateSum).grid(row=3)

mywindow.mainloop()