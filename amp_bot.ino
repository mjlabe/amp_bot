#include "amp_bot.h"
#include <VarSpeedServo.h>


Knob* amp_knobs[];

void setup() {
  const int num_knobs = sizeof(knobs)/sizeof(int);
  for (int amp_knob = 0; amp_knob < num_knobs; amp_knob++) {
    // setup global array of knob objects
    amp_knobs[amp_knob] = new Knob(knobs[i]._switch, knobs[i]._led, knobs[i]._knob);
    // Create external interrupt for pin on Change
    attachInterrupt(digitalPinToInterrupt(knobs[i]._pin), button_pressed, CHANGE);
  }
} 

class Knob(KnobValues amp_knob) {
  int _switch_pin = amp_knob._switch_pin;
  int _led_pin = amp_knob._led_pin;
  float _knob_pin = amp_knob._knob_pin;

  int _switch_state = LOW;
  float _knob_state_low = amp_knob._knob_low_value;
  float _knob_state_high = amp_knob._knob_high_value;

  void switch() {
    // change switch state and update LED
    _switch_state = (_switch_state == LOW)? HIGH: LOW;
    digitalWrite(_led_pin, _switch_state);

    float _knob_state = (_knob_state == _knob_state_low)? _knob_state_high: _knob_state_low;
    VarSpeedServo.slowmove(_knob_pin, _knob_state);
  }
}

void button_pressed() {
  // loop through all buttons and update state if changed
  const int num_knobs = sizeof(amp_knobs)/sizeof(int);
  for (int amp_knob = 0; amp_knob < num_knobs; amp_knob++) {
    state = digitalRead(amp_knobs[amp_knob]._switch);
    if (state != amp_knobs[amp_knob]._switch_state) {
      amp_knobs[amp_knob].switch()
    }
  }
}

void loop() {
  
}
