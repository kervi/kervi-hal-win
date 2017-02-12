from . import gpio
from . import i2c


def get_gpio_driver():
    return gpio.GPIODriver()

def get_i2c_driver(address, busnum=0):
    return i2c.I2CDriver(address, busnum)
