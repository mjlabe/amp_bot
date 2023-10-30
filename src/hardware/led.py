import machine, utime


class LED:
    def __init__(self, pin):
        self.led = machine.Pin(pin, machine.Pin.OUT)

    def on(self):
        self.led(1)

    def off(self):
        self.led(0)

    def flash(self, num_times: int, frequency_ms: int):
        for i in range(num_times):
            self.led.on()
            utime.sleep_ms(frequency_ms)
            self.led.off()
