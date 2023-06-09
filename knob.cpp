#include <Arduino.h>
#include <Servo.h>
#include "knob.h"

Knob::Knob(KnobValues amp_knob) {
  int _switch_pin = amp_knob._switch_pin;
  int _led_pin = amp_knob._led_pin;
  int _knob_pin = amp_knob._knob_pin;

  Servo knob_servo;
  knob_servo.attach(amp_knob._knob_pin);  // attaches the servo on _knob_pin to the servo object

  int _switch_state = LOW;
  int _knob_state_low = amp_knob._knob_low_value;
  int _knob_state_high = amp_knob._knob_high_value;
}

void Knob::switch_state() {
  // change switch state and update LED
  _switch_state = (_switch_state == LOW)? HIGH: LOW;
  digitalWrite(_led_pin, _switch_state);

  move();
}

void Knob::move() {
  int move_delay = 10;

  int _knob_state_new = map((_switch_state == LOW)? _knob_state_high : _knob_state_low, 900, 1500, 0, 180);
  int _knob_state_old = map((_switch_state == LOW)? _knob_state_low : _knob_state_high, 900, 1500, 0, 180);

  if (_switch_state == HIGH) {
    // turn knob up
    for(int pos = _knob_state_old; pos <= _knob_state_new; pos += 1) {
      knob_servo.write(pos);
      delay(move_delay);
    }
  }
  else {
    // turn knob down
    for(int pos = _knob_state_old; pos >= _knob_state_new; pos-=1) {
      knob_servo.write(pos);
      delay(move_delay);
    }
  }
}