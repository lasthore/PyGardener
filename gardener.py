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

    def stop_all_devices(self):
        for device in self.devices:
            device.stop_device()

    def start(self):
        print "starting garden loop"
        try:
            while True:
                now = datetime.today()
                self.update_all(now.hour)
                time.sleep(self.interval)
        except KeyboardInterrupt:
            self.stop_all_devices()
            print "interrupted"

    def set_update_interval(self, interval):
        self.interval = interval


def main():
    led = LightController(led_pin)
    led.set_active_time_interval(7, 21)
    my_garden = GardenScheduler("garasjen")
    my_garden.set_update_interval(300)
    my_garden.add_device(led)
    my_garden.start()

if __name__ == "__main__":
    main()