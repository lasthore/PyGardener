import RPi.GPIO as GPIO

led_pin = 22

def setup():
	GPIO.setmode(GPIO.BGCM)
	GPIO.setup(led_pin, GPIO.OUT)

class LedController(object):
	"""A controller for LED lights..."""

	def __init__(self, pin_number):
		self.pin = pin_number

	def __set_light__(self, state):
		GPIO.output(self.pin, state ? GPIO.LOW : GPIO.HIGH)
	
	def update(self, time):
		print "the time is something. Update leds"

class GardenScheduler(objcet):
	"""Scheduling garden tasks"""
	def __init__(self, name):
		self.name = name
		self.devices = []

	def add_device(self, device):
		self.devices.add(device)

	def update_all(self, time):
		for device in self.devices:
			device.update(time)
		
	def start(self):
		print "starting garden loop"
		print "schedule update_all() to run every 5 min or so?"

def main():
	setup()
	led = LedController()
	my_garden = GardenScheduler("garasjen")
	my_garden.addDevice(led)
	my_garden.start()
