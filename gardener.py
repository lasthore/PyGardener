from LightController import LightController
from datetime import datetime
import time

led_pin = 22

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
		try:
			while True:
				now = datetime.today()
				self.update_all(now.second)
				time.sleep(self.interval)
		except KeyboardInterrupt:
			print "interrupted"

	def set_update_interval(self, interval):
		self.interval = interval


def main():
	led = LightController(led_pin)
	led.set_active_time_interval(5, 35)
	my_garden = GardenScheduler("garasjen")
	my_garden.set_update_interval(5)
	my_garden.add_device(led)
	my_garden.start()

if __name__ == "__main__":
	main()