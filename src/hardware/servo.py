import machine


class Servo:
    def __init__(self, signal_pin_number, feedback_pin_number, steps=20):
        self.signal_pin = machine.Pin(signal_pin_number)
        self.feedback_pin = machine.Pin(feedback_pin_number)
        self.servo = machine.PWM(self.signal_pin, freq=50)
        self.position = self.get()
        self.steps = steps

    def get(self):
        # TO DO
        self.feedback_pin
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

