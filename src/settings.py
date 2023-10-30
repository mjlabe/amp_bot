import ujson


# set switch pins in ascending order
SWITCH_PINS = [16, 17, 22]

# set servo pins in ascending order (SIG, FDBK)
SERVO_PINS = [
    (26, 34, ),
    (27, 35, ),
    (14, 32, ),
    (12, 33, ),
    (13, 25, ),
]


def load_saved_settings():
    # load settings as {SWITCH_PIN: {(SERVO_SGNL_PIN, SERVO_FDBK_PIN): SERVO_ANGLE}}
    user_settings = {i: {j: 90 for j in SERVO_PINS} for i in SWITCH_PINS}
    try:
        with open("settings.json", "rb") as settings_file:
            user_settings |= ujson.load(settings_file)
    except Exception:
        pass
    return user_settings
