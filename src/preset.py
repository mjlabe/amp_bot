import ujson

from src.hardware.servo import Servo
from src.hardware.switch import Switch
from src.settings import load_saved_settings


class Preset(Switch):
    def __init__(self, switch_pin: int):
        self.preset = self.get_preset()
        super().__init__(switch_pin)
        self.switch = switch_pin
        self.servos = []
        for servo, _ in self.preset:
            # get signal and feedback pins for all servos
            servo = Servo(servo[0], servo[1])
            # set to noon on startup
            servo.set(90)
            self.servos.append(servo)

    def handler(self, time_held):
        if time_held > self.time_to_hold_ms:
            self.save_preset()
        else:
            for servo in self.servos:
                servo.set(self.preset)

    def get_preset(self):
        presets = load_saved_settings()
        return presets[self.switch]

    def save_preset(self):
        preset = {(servo.signal_pin, servo.feedback_pin): servo.get() for servo in self.servos}
        presets = load_saved_settings()
        presets[self.switch] = preset
        with open("settings.json", "wb") as settings_file:
            ujson.dump(presets, settings_file, indent=4)
