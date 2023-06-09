#include "knob.h"

// list of knobs {foot_switch_pin, led_pin, knob_servo_pin, knob_clock_value_low, knob_clock_value_high}
KnobValues knobs[] = {
  // gain
  {1, 12, 14, 900, 1000},
  // bass
  {2, 16, 18, 1200, 1300},
  // // mids
  // {1, 12, 14},
  // // treble
  // {2, 16, 18},
  // // volume
  // {2, 16, 18},
};
