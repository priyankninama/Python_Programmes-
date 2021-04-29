# import everything from tkinter module
from tkinter import *
import tkinter.messagebox

root = tkinter.Tk()

root.title("Practical 32")
root.geometry('400x200')

def onClick():
	tkinter.messagebox.showinfo("Hello", "Thank You For Clicking")

button = Button(root, text="Click Me", command=onClick, height=5, width=10)

button.pack()
root.mainloop()
