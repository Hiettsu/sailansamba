 #moottoriohjaus
 #L1= io26 ruskea
 #L2= io19 punainen
 #L3= io6 oranssi
 #L4= io5 keltavihreä

import time
import RPi.GPIO as io
io.setwarnings(False)
io.setmode(io.BCM)

def forward1():
	io.output(26, io.HIGH)
	io.output(19, io.LOW)
	
def forward2():
	io.output(5, io.HIGH)
	io.output(6, io.LOW)
	
def backward1():
	io.output(19, io.HIGH)
	io.output(26, io.LOW)

def backward2():
	io.output(6, io.HIGH)
	io.output(5. io.LOW)

def setup():
	io.setup(26, io.OUT)
	io.setup(19, io.OUT)
	io.setup(6, io.OUT)
	io.setup(5, io.OUT)

def stop():
	io.output(26, io.LOW)
	io.output(19, io.LOW)
	io.output(6, io.LOW)
	io.output(5, io.LOW)

setup()
print("Aloitetaan")

while True
	print("moottori 1 eteen ja moottori 2 taakse")
	forward1()
	backward2()
	time.sleep(10)
	print("moottori 1 taakse ja moottori 2 eteen")
	backward1()
	forward2()
	time.sleep(10)
