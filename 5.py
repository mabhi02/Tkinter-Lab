from tkinter import *

app = Tk()
app.title("GUI Example 5")
app.geometry('400x400')


def exitApp():
    app.destroy()

def giveHelp():
    ans = messagebox.askquestion("Not Much Help", "Are you sure you need help", \
                    default=messagebox.NO)
    print(ans)

def aboutMsg():
    messagebox.showinfo("About Exercise 5", "Exercise 5 covers menus and dialogs")

def openFile():
    filename = filedialog.askopenfilename( \
        title="Choose a file to open", \
        filetypes=[("Text","*.txt"), ("All", "*")] )
    print(filename)
    


menuBar = Menu(app)
app.winfo_toplevel()['menu'] = menuBar

file = Menu(menuBar)
file.add_command(label='Open', command=openFile)
file.add_command(label='Quit', command=exitApp)
menuBar.add_cascade(label="File", menu=file)

hlp = Menu(menuBar)
hlp.add_command(label='Help', command=giveHelp)
hlp.add_command(label='About', command=aboutMsg)
menuBar.add_cascade(label="Help", menu=hlp)

app.mainloop()

