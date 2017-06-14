try:
    import RPi.GPIO as GPIO
except ImportError:
    import GPIOMock as GPIO

class LightController(object):
    def __init__(self, pin_number):
        self.pin = pin_number
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

    def __set_light_active__(self, state):
        GPIO.output(self.pin, GPIO.LOW if state else GPIO.HIGH)

    def update(self, time):
        self.__set_light_active__(True if time in range(self.start, self.stop) else False)

    def stop_device(self):
        GPIO.cleanup()

    def set_active_time_interval(self, start, stop):
        self.start = start
        self.stop = stop
