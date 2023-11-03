import ujson

import settings

from src.hardware.led import LED
from src.hardware.servo import Servo
from src.hardware.switch import Switch


class Preset(Switch):
    def __init__(self, switch_pin: int):
        self.preset = self.load_preset()
        super().__init__(switch_pin)
        self.switch = switch_pin
        self.led = LED(self.preset["led"])
        self.servos = []
        for settings, _ in self.preset:
            # get signal and feedback pins for all servos
            servo = Servo(settings["servo"][0], settings["servo"][1])
            # set to noon on startup
            servo.set(90)
            self.servos.append(servo)

    def handler(self, time_held):
        if time_held > self.time_to_hold_ms:
            self.save_preset()
        else:
            for servo in self.servos:
                servo.set(self.preset)

    def load_preset(self):
        presets = self.load_presets()
        return presets[self.switch]

    def save_preset(self):
        preset = {
            (servo.signal_pin, servo.feedback_pin): servo.get() for servo in self.servos
        }
        presets = self.load_presets()
        presets[self.switch] = preset
        with open("settings.json", "wb") as settings_file:
            ujson.dump(presets, settings_file, indent=4)
        # flash to notify user preset is saved
        self.led.flash(num_times=5, frequency_ms=500)

    @staticmethod
    def load_presets():
        # load settings as {SWITCH_PIN: {(SERVO_SGNL_PIN, SERVO_FDBK_PIN): SERVO_ANGLE}}
        user_settings = {
            i[0]: {
                "led": i[1],
                "servos": {j: 90 for j in settings.SERVO_PINS}
            }
            for i in settings.SWITCH_PINS
        }
        try:
            with open("settings.json", "rb") as settings_file:
                user_settings |= ujson.load(settings_file)
        except Exception:
            pass
        return user_settings
