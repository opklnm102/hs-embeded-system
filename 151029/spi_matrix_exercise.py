import RPi.GPIO as GPIO
import max7219.led as led
import time

xpos = 0
ypos = 3

def button_pressed_left(channel):
	global xpos
	global ypos

	device.pixel(xpos,ypos,0)
	
	if xpos == 0:
		xpos = 7
	else:
		xpos = xpos -1

	device.pixel(xpos,ypos,1)

def button_pressed_right(channel):
	global xpos
	global ypos

	device.pixel(xpos,ypos,0)

	if xpos == 7:
		xpos = 0
	else:
		xpos = xpos +1

	device.pixel(xpos,ypos,1)
	
def button_pressed_up(channel):
	global xpos
	global ypos

	device.pixel(xpos,ypos,0)

	if ypos == 7:
		ypos = 0
	else:
		ypos = ypos + 1

	device.pixel(xpos,ypos,1)

def button_pressed_down(channel):
	global xpos
	global ypos

	device.pixel(xpos,ypos,0)

	if ypos == 0:
		ypos = 7
	else:
		ypos = ypos -1

	device.pixel(xpos,ypos,1)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
button_left = 19 
button_right = 20
button_up = 21
button_down = 26

GPIO.setup(button_left, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(button_right, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(button_up, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(button_down, GPIO.IN, GPIO.PUD_UP)

GPIO.add_event_detect(button_left, GPIO.RISING, bouncetime=200)  #rising edge detection
GPIO.add_event_detect(button_right, GPIO.RISING, bouncetime=200)  #rising edge detection
GPIO.add_event_detect(button_up, GPIO.RISING, bouncetime=200)  #rising edge detection
GPIO.add_event_detect(button_down, GPIO.RISING, bouncetime=200)  #rising edge detection

GPIO.add_event_callback(button_left, button_pressed_left)  #callback
GPIO.add_event_callback(button_right, button_pressed_right)  #callback
GPIO.add_event_callback(button_up, button_pressed_up)  #callback
GPIO.add_event_callback(button_down, button_pressed_down)  #callback


device = led.matrix()
#device.show_message("Hello world!")

device.pixel(xpos,ypos,1) 

while True:
	continue
