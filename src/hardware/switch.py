import machine, utime
from src.settings import save, SERVO_PINS
from src.hardware.servo import Servo


class Switch:
    def __init__(self, pin, interrupt=False):
        self.switch = machine.Pin(pin, machine.Pin.IN, machine.Pin.PULL_UP)
        self.presses = 0
        if interrupt:
            self.switch.irq(trigger=machine.Pin.IRQ_FALLING, handler=self._handler)

    def handler(self, held=0):
        raise NotImplementedError("Switch is an abstract class and the handler method needs to be defined.")

    def _handler(self, held=0):
        self._debounce()
        self.handler(held)

    def _debounce(self, hold_length_s=5):
        # disable the IRQ during our debounce check
        self.switch.irq(handler=None)
        # debounce time - we ignore any activity during this period
        held_length_s = 0
        while held_length_s < hold_length_s:
            utime.sleep_ms(200)
            if self.switch.value() != 0:
                # re-enable the IRQ
                self.switch.irq(trigger=machine.Pin.IRQ_FALLING, handler=self._handler)
                return
        self.save_preset()

    def save_preset(self):
        # read servo values
        preset_settings = {}
        for pin in SERVO_PINS:
            servo = Servo(pin_number=pin)
            preset_settings[pin] = servo.get()
        # save values
        if preset_settings:
            save(self.switch, preset_settings)
        else:
            # flash LED to show error
            pass


