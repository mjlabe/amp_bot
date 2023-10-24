import ujson


# set switch pins in ascending order
SWITCH_PINS = [23, 25, 27]

# set servo pins in ascending order
SERVO_PINS = [12, 14, 15, 16, 17]


def load():
    user_settings = {i: {j: 0 for j in SERVO_PINS} for i in SWITCH_PINS}
    try:
        with open("settings.json", "rb") as settings_file:
            user_settings |= ujson.load(settings_file)
    except Exception:
        pass
    return user_settings

# needs https://www.adafruit.com/product/1449
def save(switch, user_settings):
    settings[switch] = user_settings
    with open("settings.json", "wb") as settings_file:
        ujson.dump(settings, settings_file, indent=4)

settings = load()
