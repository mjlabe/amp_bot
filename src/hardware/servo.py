import machine


class Servo:
    def __init__(self, pin_number, steps=20):
        pin = machine.Pin(pin_number)
        self.servo = machine.PWM(pin, freq=50)
        self.position = self.get()
        self.steps = steps

    def get(self):
        # TO DO
        return 0

    def set(self, angle):
        self.position = angle
        self._set_with_speed(angle)

    def _set_with_speed(self, angle):
        duty_cycle_delta = (angle - self.position) / self.steps
        while self.position != angle:
            if self.position > angle:
                duty_cycle_delta = -duty_cycle_delta
            self.position = self.position + duty_cycle_delta
            self.servo.ChangeDutyCycle(self.position)

