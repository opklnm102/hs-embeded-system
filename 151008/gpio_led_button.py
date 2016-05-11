import RPi.GPIO as GPIO
import time

def button_pressed(channel):
	GPIO.output(led,1)
	time.sleep(2)
	GPIO.output(led,0)
	

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 23 #GPIO channel number
GPIO.setup(led, GPIO.OUT)

button = 21
GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)
GPIO.add_event_detect(button, GPIO.RISING, bouncetime=200)
GPIO.add_event_callback(button, button_pressed)

while True:
	continue
