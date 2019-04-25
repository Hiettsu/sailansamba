import tkinter as tk
import os



win = tk.Tk()

win.title("Ikkuna")

def motor():
    os.system('python motor.py')

def reset():
    os.system('python reset.py')

b = tk.Button(win, text="Motor", command=motor)
b.pack()

c = tk.Button(win, text="Reset", command=reset)
c.pack()

win.resizable()

win.mainloop()
