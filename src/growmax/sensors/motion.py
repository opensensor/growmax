from machine import Pin, Timer


class MotionSensor:
    """ Detect motion and remain on for a configurable duration of time.
    """

    def __init__(self, pin, duration_ms=10000, callback=None):
        self.pin = pin
        self.pin.irq(handler=self._switch_change, trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING)
        self.debounce_timer = Timer(-1)
        self.last_value = pin.value()
        self.duration_ms = duration_ms
        self.callback = callback

    def value(self):
        return self.last_value

    def _switch_change(self, pin):
        self.last_value = pin.value()
        if self.last_value and self.callback:
            self.callback(self)
        self._start_switch_timer()

    def _start_switch_timer(self):
        self.debounce_timer.init(period=self.duration_ms, mode=Timer.ONE_SHOT,
                                 callback=self._check_switch)

    def _check_switch(self, _):
        # Re-enable the Switch IRQ to get the next change
        self.last_value = self.pin.value()
        if self.callback:
            self.callback(self)


