# boot.py
import micropython

from settings import load_saved_settings
from src.preset import Preset

micropython.alloc_emergency_exception_buf(100)


def init():
    settings = load_saved_settings()
    for pin, setting in settings:
        # init preset interrupt
        preset = Preset(pin)
        preset.led.flash(1, 1000)


if __name__ == "__main__":
    init()