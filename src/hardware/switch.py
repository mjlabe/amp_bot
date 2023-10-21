import machine, utime


class Switch:
    def __init__(self, pin, interrupt=False):
        self.switch = machine.Pin(pin, machine.Pin.IN, machine.Pin.PULL_UP)
        self.presses = 0
        if interrupt:
            self.switch.irq(trigger=machine.Pin.IRQ_FALLING, handler=self._handler)

    def handler(self):
        raise NotImplementedError("Switch is an abstract class and the handler method needs to be defined.")

    def _handler(self):
        self._debounce()
        self.handler()

    def _debounce(self):
        # disable the IRQ during our debounce check
        self.switch.irq(handler=None)
        # debounce time - we ignore any activity diring this period
        utime.sleep_ms(200)
        # re-enable the IRQ
        self.switch.irq(trigger=machine.Pin.IRQ_FALLING, handler=self._handler)
