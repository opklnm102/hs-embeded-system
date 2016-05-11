import RPi.GPIO as GPIO
import time

def button_ledOn_pressed(channel):
	GPIO.output(led,1)

def button_ledOff_pressed(channel):
	GPIO.output(led,0)
	

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 23
GPIO.setup(led, GPIO.OUT)

button_ledOn = 21
GPIO.setup(button_ledOn, GPIO.IN, GPIO.PUD_UP)
GPIO.add_event_detect(button_ledOn, GPIO.RISING, bouncetime = 200)
GPIO.add_event_callback(button_ledOn, button_ledOn_pressed)

button_ledOff = 24
GPIO.setup(button_ledOff, GPIO.IN, GPIO.PUD_UP)
GPIO.add_event_detect(button_ledOff, GPIO.RISING, bouncetime = 200)
GPIO.add_event_callback(button_ledOff, button_ledOff_pressed)

while True:
	continue
