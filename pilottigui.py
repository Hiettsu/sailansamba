from tkinter import *
import tkinter as tk
import time
import RPi.GPIO as io
io.setwarnings(False)
io.setmode(io.BCM)

io.setup(26, io.OUT)
io.setup(19, io.OUT)
print("Motors has been set up")

def function1():
    

    
    io.output(26, io.HIGH)
    io.output(19, io.LOW)
    time.sleep(5)
    io.output(19, io.HIGH)
    io.output(26, io.LOW)
    time.sleep(5)
    print ("Eteen")
    while Trust:
        break

def function1_background():
    t = threading.Thread(target=function1)
    t.start()

def function2():
    io.output(26, io.LOW)
    io.output(19, io.HIGH)
    print ("testi")

def function2_backround():
    t = threading.Thread(target=function2)
    t.start()

def function3():
    io.output(26, io.LOW)
    io.output(19, io.LOW)
    print("stopped")

def function3_backround():
    t = threading.Thread(target=function3)
    t.start()

root = Tk()

w = 450 # width for the Tk root
h = 500# height for the Tk root

frame = Frame(root, width=w,height =h)
button1 = Button(frame, text = 'function 1', fg='black', command=function1).grid(row=1,column=1)
button1 = Button(frame, text='function 1', fg='black', command=function1_background)
button2 = Button(frame, text = 'function 2',fg='black',command=function2).grid(row=1,column=2)
button2 = Button(frame, text ='function 2', fg='black',command=function2_backround)
button3 = Button(frame, text = 'function 3', fg='red',command=function3).grid(row=1,column=4)
button3 = Button(frame, text ='function 3', fg='red',command=function3_backround)

frame.pack()
root.mainloop()
