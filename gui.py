from tkinter import *
from tkinter import filedialog


def new_file():
    text.delete(0.0, END)


def open_file():
    file1 = filedialog.askopenfile(mode='r')
    data = file1.read()
    text.delete(0.0, END)
    text.insert(0.0, data)

def save_file():
    filename = "OBIOS Notes.txt"
    data = txt.get(0.0, END)
    file1 = open(filename, 'w')
    file1.write(data)


def save_as():
    file1 = filedialog.asksaveasfile(mode-'w')
    data = text.get(0.0, END)
    file1.write(data)


# Interface 
gui = Tk()
gui.title("OBIOS Notepad (Python Ed)")
gui.geometry("600x500")
text = Text(gui)
text.pack()

# Menu
mymenu = Menu()
list1 = Menu()
list1.add_command(label="New file", command=new_file)
list1.add_command(label="Open file", command=open_file)
list1.add_command(label="Save", command=save_file)
list1.add_command(label="New file", command=save_as)
list1.add_command(label="Exit", command=gui.quit)

mymenu.add_cascade(label="File", menu=list1)
mymenu.add_cascade(label="Exit", command=gui.quit)
gui.config(menu=mymenu)
gui.mainloop()