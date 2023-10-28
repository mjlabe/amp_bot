import ujson

from src.hardware.servo import Servo
from src.hardware.switch import Switch
from src.settings import load_saved_settings


class Preset(Switch):
    def __init__(self, switch_pin: int, servo_pins: [int], pin):
        self.preset_values = self.get_preset_values()
        super().__init__(pin)
        self.switch = switch_pin
        self.servos = []
        for servo_pin in servo_pins:
            servo = Servo(servo_pin)
            # set to noon on startup
            servo.set(90)
            self.servos.append(servo)

    def handler(self, time_held):
        if time_held > self.time_to_hold_ms:
            self.save_preset()
        else:
            for servo in self.servos:
                servo.set(self.preset_values)

    @staticmethod
    def get_preset_values():
        return load_saved_settings()

    def save_preset(self):
        settings = {"TO": "DO"}
        with open("settings.json", "wb") as settings_file:
            ujson.dump(settings, settings_file, indent=4)
