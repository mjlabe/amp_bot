struct KnobValues {
  int _switch_pin;
  int _led_pin;
  int _knob_pin;
  int _knob_low_value;
  int _knob_high_value;
};

class Knob {
  public:
      Knob(KnobValues);
      void switch_state();
      void move();
      int _switch_pin;
      int _led_pin;
      int _knob_pin;
      Servo knob_servo;
      int _switch_state;
      int _knob_state_low;
      int _knob_state_high;
};
