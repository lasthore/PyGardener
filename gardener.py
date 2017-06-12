import RPi.GPIO as GPIO

led_pin = 22

def setup():
	GPIO.setmode(GPIO.BGCM)
	GPIO.setup(led_pin, GPIO.OUT)

def set_light(state):
	GPIO.output(led_pin, GPIO.LOW)


