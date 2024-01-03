from tkinter import *
import sys

# Initializes Root
root = Tk()
root.title('Notes')
root.geometry('300x300')
root.resizable(False, False)

# Defines functions for buttons
def exit():
    sys.exit()
def save():
    noteContent = t.get('1.0', 'end')
    f = open('savednote.txt', 'w')
    f.write(noteContent)
def load():
    f = open('savednote.txt')
    noteContent = f.read()
    t.delete('1.0', 'end')
    t.insert('1.0', noteContent)

# Creates widgets
exitButton = Button(root, text = ' X ', command = exit)
saveButton = Button(root, text = 'save', command = save)
loadButton = Button(root, text = 'load', command = load)
t = Text(root)

# Inserts widgets into the program
exitButton.grid(row = 0, column = 0)
saveButton.grid(row = 0, column = 1)
loadButton.grid(row = 0, column = 2)
t.place(x = 0, y = 25, width = 300, height = 300)

root.mainloop()