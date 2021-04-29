from tkinter import *
from random import  choice

top = Tk()
top.title("Background color")
c = Canvas(top, height=400, width=400 )

button1 = Button(top, text="Red", anchor = CENTER, font = 'bold', command=lambda: c.configure(bg= "red"))
button1.configure(width = 10, activebackground= "red", relief=SUNKEN)

button2 = Button(top, text="Green", anchor = CENTER, font = 'bold', command=lambda: c.configure(bg= "green"))
button2.configure(width = 10, activebackground = "green", relief=SUNKEN)


button3 = Button(top, text="Blue", anchor = CENTER, font = 'bold', command=lambda: c.configure(bg= "blue"))
button3.configure(width = 10, activebackground = "blue", relief=SUNKEN)

button1_window = c.create_window(10, 20, anchor = NW, window = button1)
button2_window = c.create_window(110, 20, anchor = NW, window = button2)
button3_window = c.create_window(210, 20, anchor = NW, window = button3)

c.pack()
top.mainloop()