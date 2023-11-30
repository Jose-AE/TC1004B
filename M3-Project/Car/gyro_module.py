from gpiozero import DigitalInputDevice
import time

#  GPIO pins
pin_z = 26

sensor_z = DigitalInputDevice(pin=pin_z, pull_up=False)


def read_z():
    return sensor_z.value
