#include <Arduino.h>
#include <Servo.h>
#include "amp_bot.h"


Knob* amp_knobs[12];

void setup() {
  const int num_knobs = sizeof(knobs)/sizeof(int);
  for (int amp_knob = 0; amp_knob < num_knobs; amp_knob++) {
    // setup global array of knob objects
    KnobValues knob_values = {knobs[amp_knob]._switch_pin, knobs[amp_knob]._led_pin, knobs[amp_knob]._knob_pin};
    amp_knobs[amp_knob] = new Knob(knob_values);
    // Create external interrupt for pin on Change
    pinMode(knobs[amp_knob]._switch_pin, INPUT);
    pinMode(knobs[amp_knob]._led_pin, OUTPUT);
    pinMode(knobs[amp_knob]._knob_pin, OUTPUT);
    attachInterrupt(digitalPinToInterrupt(knobs[amp_knob]._switch_pin), button_pressed, CHANGE);
  }
}

void button_pressed() {
  // loop through all buttons and update state if changed
  const int num_knobs = sizeof(amp_knobs)/sizeof(int);
  for (int amp_knob = 0; amp_knob < num_knobs; amp_knob++) {
    int state = digitalRead(amp_knobs[amp_knob] -> _switch_pin);
    if (state != amp_knobs[amp_knob] -> _switch_state) {
      amp_knobs[amp_knob] -> switch_state();
    } 
  }
}

void loop() {
  
}
