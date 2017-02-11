class GPIODriver(object):
    def __init__(self):
        print("init gpio driver")

    def define_pin_in(self, pin):
        print("define pin in")

    def define_pin_out(self, pin):
        print("define pin out")

    def define_pin_pwm(self, pin, frequency):
        print("define pwm")

    def set_pin_low(self, pin):
        print("set pin low")

    def set_pin_high(self, pin):
        print("set pin high")

    def get_pin(self, pin):
        print("get pin")
        return 0

    def start_pwm(self, pin, duty_cycle):
        print("start pwm")

    def stop_pwm(self, pin):
        print("stop pwm")

    def listen_rising_pin(self, pin, callback):
        print("listen rising")

    def listen_falling_pin(self, pin, callback):
        print("listen falling")
