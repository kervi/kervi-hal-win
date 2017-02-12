from kervi.utility.hal.gpio import IGPIODeviceDriver

class GPIODriver(IGPIODeviceDriver):
    def __init__(self):
        print("init win gpio driver")

    def define_as_input(self, pin):
        print("define pin in")

    def define_as_output(self, pin):
        print("define pin out")

    def define_as_pwm(self, pin, frequency):
        print("define pwm")

    def set(self, pin, state):
        print("set pin low")

    def get(self, pin):
        print("get pin")
        return 0

    def start_pwm(self, pin, duty_cycle, frequency=None):
        print("start pwm")

    def stop_pwm(self, pin):
        print("stop pwm")

    def listen(self, pin, callback, bounce_time=0):
        print("listen rising")

    def listen_rising(self, pin, callback, bounce_time=0):
        print("listen rising")

    def listen_falling(self, pin, callback, bounce_time=0):
        print("listen falling")
