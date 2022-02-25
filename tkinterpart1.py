# Import the Tkinter package
# Note in Python 3 it is all lowercase
from tkinter import *
# This method is called when the button is pressed
def clicked():
    print("Changed Clicked")
# Create a main frame with
# - a title
# - size 200 by 200 pixels
app = Tk()
app.title("GUI Changed Example 1")
app.geometry('800x800')
# Create the button with
# - suitable text
# - a command to call when the button is pressed
button1 = Button(app, text="Changed Click Here", command=clicked)
# Make the button visible at the bottom of the frame
button1.pack(side='top')
# Start the application running
app.mainloop()