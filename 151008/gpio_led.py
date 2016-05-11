import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 24 # GPIO channel number

GPIO.setup(led, GPIO.OUT)

GPIO.output(led, 1)
time.sleep(2)
GPIO.output(led, 0) 
