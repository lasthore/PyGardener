#import RPi.GPIO as GPIO

led_pin = 22

def setup():
	#GPIO.setmode(GPIO.BGCM)
	#GPIO.setup(led_pin, GPIO.OUT)

class LedController(object):
	"""A controller for LED lights..."""

	def __init__(self, pin_number):
		self.pin = pin_number

	def __set_light__(self, state):
        print #GPIO.output(self.pin, state ? GPIO.LOW : GPIO.HIGH)
	
	def update(self, time):
		print "the time is something. Update leds"
		print time

class LedMock(object):
    def __init__(self, pin_number):
        self.pin = pin_number

    def __set_light__(self, state):
        print "GPIO.output(self.pin, state ? GPIO.LOW: GPIO.HIGH)"

        def update(self, time):
            print "the time is something. Update leds"
            print time

class GardenScheduler(object):
	"""Scheduling garden tasks"""

	def __init__(self, name):
		self.name = name
		self.devices = []

	def add_device(self, device):
		self.devices.append(device)

	def update_all(self, time):
		for device in self.devices:
			device.update(time)
		
	def start(self):
		print "starting garden loop"
		print "schedule update_all() to run every 5 min or so?"

	def set_on_interval(self, start, stop):
		self.start = start
		self.stop = stop


def main(self):
	setup()
	led = LedMock(led_pin)
	led.set_on_interval(700, 2100)
	my_garden = GardenScheduler("garasjen")
	my_garden.addDevice(led)
	my_garden.start()
