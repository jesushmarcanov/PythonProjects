#RELOJ DIGITAL EN PYTHON
from tkinter import *
from time import strftime 

root = Tk()
root.title("Reloj Digital")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(
    root,
    font=('Courier',60),
    background='black',
    foreground='cyan')

label.pack(anchor='center')

time()
root.mainloop()