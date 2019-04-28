from tkinter import *
import tkinter as tk
import time
import RPi.GPIO as io
from threading import *
import threading
from PIL import ImageTk,Image
 
def asetukset():
   
    io.setwarnings(False)
    io.setmode(io.BCM)
    io.setup(26, io.OUT)
    io.setup(19, io.OUT)
    io.setup(6, io.OUT)
    io.setup(5, io.OUT)
    print("Motors has been set up")
 
def asetukset_backround():
    t = threading.Thread(target=asetukset)
    t.start()
 
def function1a():
    global callback
    io.output(26, io.HIGH)
    io.output(19, io.LOW)
    io.output(6, io.HIGH)
    io.output(5, io.LOW)
    callback = root.after(5000, function1b)
    print ("Eteen")
 
def function1b():
    io.output(19, io.HIGH)
    io.output(26, io.LOW)
    io.output(6, io.LOW)
    io.output(5, io.HIGH)
    callback = root.after(5000, function1a)
 
def function1a_background():
    t = threading.Thread(target=function1a)
    t.start()
 
def function2():
    io.output(26, io.LOW)
    io.output(19, io.HIGH)
    io.output(5, io.LOW)
    io.output(6, io.HIGH)
    root.after(3000)
    print ("Kaikki alas")
 
def function2_backround():
    t = threading.Thread(target=function2)
    t.start()
 
def function3():
    io.output(26, io.LOW)
    io.output(19, io.LOW)
    io.output(5, io.LOW)
    io.output(6, io.LOW)
    root.after_cancel (callback)
   
    print("Lopetettu")
 
def function3_backround():
    t = threading.Thread(target=function3)
    t.start()
 
 
def function4():
    io.output(26, io.HIGH)
    io.output(19, io.LOW)
    io.output(6, io.LOW)
    io.output(5, io.HIGH)
    print("Kaikki eteen")
 
def function4_backround():
    t = threading.Thread(target=function4)
    t.start()
 
 
 
 
root = Tk()
root.title('Moottorien Ohjaus')
 
w = 1920# width for the Tk root
h = 1080# height for the Tk root
 
frame = Frame(root, width=w,height =h)
button1 = Button(frame, text = 'Automaattinen moottorin ohjaus', fg='black', command=function1a).grid(row=1,column=1)
button1 = Button(frame, text='Automaattinen moottorin ohjaus', fg='black', command=function1a_background)
 
button2 = Button(frame, text = 'Moottorit ala-asentoon',fg='black',command=function2).grid(row=2,column=2)
button2 = Button(frame, text ='Moottorit ala-asentoon', fg='black',command=function2_backround)
 
button3 = Button(frame, text = 'Hätäseis', fg='red',command=function3).grid(row=1,column=4)
button3 = Button(frame, text ='Hätäseis', fg='red',command=function3_backround)
 
button4 = Button(frame, text='Kalibroi automaattisesti', fg='black',command=asetukset).grid(row=2,column=1)
button4 = Button(frame, text ='Kalibroi automaattisesti', fg='black',command=asetukset_backround)
 
button5 = Button(frame, text='Moottorit ylä-asentoon', fg='black',command=function4).grid(row=1,column=2)
button5 = Button(frame, text ='Moottorit ylä-asentoon', fg='black',command=function4_backround)
 
 
 
canvas = Canvas(root, width = 1280, height = 958)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("nytmeni.jpg"))  
canvas.create_image(20, 20, anchor=NW, image=img)  
 
frame.pack()
root.mainloop()
