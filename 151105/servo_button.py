import RPi.GPIO as GPIO
import time
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)

pwm = GPIO.PWM(19, 50) # 50Hz
pwm.start(1)

def button_pressed(channel):
	if channel == 16:
		ms = float(1)
		dcycle = ms / 20.0 * 100
		pwm.ChangeDutyCycle(dcycle)
		print 'button 16'
	elif channel == 20:
		ms = float(1.5)
		dcycle = ms / 20.0 * 100
		pwm.ChangeDutyCycle(dcycle)
		print 'button 20'

	elif channel == 21:
		ms = float(2)
		dcycle = ms / 20.0 * 100
		pwm.ChangeDutyCycle(dcycle)
		print 'button 21'

button1 = 16
button2 = 20
button3 = 21

GPIO.setup(button1, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(button2, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(button3, GPIO.IN, GPIO.PUD_UP)

GPIO.add_event_detect(button1, GPIO.RISING, bouncetime=200) # rising edge detection
GPIO.add_event_detect(button2, GPIO.RISING, bouncetime=200) # rising edge detection
GPIO.add_event_detect(button3, GPIO.RISING, bouncetime=200) # rising edge detection

GPIO.add_event_callback(button1, button_pressed) # callback
GPIO.add_event_callback(button2, button_pressed) # callback
GPIO.add_event_callback(button3, button_pressed) # callback



time.sleep(2)

while True:
	continue

