

from tkinter import *

app = Tk() 
app.title("GUI Example 4")
app.geometry('400x400')  

w = Canvas(app, bg='blue') 
w.pack(expand = 1, fill = BOTH)


w.create_rectangle(10, 10, 100, 50, outline="red", width = 5)
w.create_rectangle(50, 150, 100, 200, fill="yellow")
w.create_oval(140, 110, 200, 170, outline="green", width = 5)
w.create_text(200, 200, text = "Hello")


def hKey(event):
    print("Lower case h key pressed")


app.bind("<KeyPress-h>", hKey)


def mouseClick(event):
    print("Mouse click at x =", event.x, "y =", event.y)
    

w.bind("<Button-1>", mouseClick)


app.mainloop() 
