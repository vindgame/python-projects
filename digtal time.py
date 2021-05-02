from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Digital Clock")

def time():
    string = strftime('%H:%M:%S%p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("ds-digital",150), background = "#424949", foreground = "#D0D3D4")
label.pack(anchor='center')
time()

mainloop()
