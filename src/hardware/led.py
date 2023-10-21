import machine


class LED:
    def __init__(self, pin):
        self.led = machine.Pin(pin, machine.Pin.OUT)

    def on(self):
        self.led(1)

    def off(self):
        self.led(0)