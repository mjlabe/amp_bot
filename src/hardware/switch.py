import machine, utime
from src.settings import save, SERVO_PINS
from src.hardware.servo import Servo


class Switch:
    def __init__(self, pin, time_to_hold_ms=5000):
        self.switch = machine.Pin(pin, machine.Pin.IN, machine.Pin.PULL_UP)
        self.time_to_hold_ms = time_to_hold_ms
        self.switch.irq(trigger=machine.Pin.IRQ_FALLING, handler=self._handler)

    def handler(self, time_held):
        raise NotImplementedError("Switch is an abstract class and the handler method needs to be defined.")

    def _handler(self):
        self._debounce()
        self.handler(self._wait_for_pin_change())

    def _debounce(self):
        # disable the IRQ during our debounce check
        self.switch.irq(handler=None)
        # wait for pin to change value
        # it needs to be stable for a continuous 20ms
        cur_value = self.switch.value()
        active = 0
        while active < 20:
            if self.switch.value() != cur_value:
                active += 1
            else:
                active = 0
            utime.sleep_ms(1)

    def _wait_for_pin_change(self) -> int:
        time_held_ms = 0
        utime.sleep_ms(20)
        while time_held_ms < self.time_to_hold_ms:
            utime.sleep_ms(20)
            time_held_ms += 20
            if self.switch.value() != 0:
                # re-enable the IRQ
                self.switch.irq(trigger=machine.Pin.IRQ_FALLING, handler=self._handler)
        return time_held_ms
