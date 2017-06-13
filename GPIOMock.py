
BGCM = "BGCM"
IN = "IN"
OUT = "OUT"
LOW = "LOW"
HIGH = "HIGH"

def setmode(mode):
    print "Setting mode to " + mode
    return None


def setup(pin, direction):
    print "Setup pin [" + str(pin) + "] in direction [" + direction + "]"
    return None


def output(pin, state):
    print "Set pin output " + str(pin) + ":" + str(state)
    return None