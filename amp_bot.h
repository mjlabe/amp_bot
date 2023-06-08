struct KnobValues {
  int _switch_pin;
  int _led_pin;
  int _knob_pin;
  float _knob_low_value;
  float _knob_high_value;
};

// list of knobs {foot_switch_pin, led_pin, knob_servo_pin, knob_clock_value_low, knob_clock_value_high}
KnobValues knobs[] = {
  // gain
  {1, 12, 14, 9.0, 10.0},
  // bass
  {2, 16, 18, 12.0, 13.0},
  // // mids
  // {1, 12, 14},
  // // treble
  // {2, 16, 18},
  // // volume
  // {2, 16, 18},
};
