# This pump class was derived from the pimoroni grow-python project released under MIT license
# Modified by opensensor.io to work with Pico Grow Max boards
# The original class was written to require Raspberry Pi OS and is available
# here:  https://github.com/pimoroni/grow-python/blob/master/library/grow/pump.py
import machine
import time

PUMP_PWM_FREQ = 10000
PUMP_MAX_DUTY = 65535


class Pump(object):
    """Grow pump driver."""

    def __init__(self, channel=1):
        """Create a new pump.
        Uses soft PWM to drive a Grow pump.
        :param channel: One of 1, 2 or 3.
        """
        self._speed = 0
        self._pin = [2, 3, 4, 5, 6, 7, 8, 9][channel - 1]
        self._gpio_pin = machine.Pin(self._pin)

        self._pwm = machine.PWM(self._gpio_pin)
        self._pwm.freq(PUMP_PWM_FREQ)
        self._pwm.duty_u16(0)

        self._timeout = None

    def _stop(self):
        self._pwm.duty_u16(0)

    def set_speed(self, speed):
        """Set pump speed (PWM duty cycle)."""
        if speed > 1.0 or speed < 0:
            raise ValueError("Speed must be between 0 and 1")

        self._pwm.duty_u16(int(PUMP_MAX_DUTY * speed))
        self._speed = speed
        return True

    def get_speed(self):
        """Return Pump speed (PWM duty cycle)."""
        return self._speed

    def stop(self):
        """Stop the pump."""
        if self._timeout is not None:
            self._timeout.cancel()
            self._timeout = None
        self.set_speed(0)

    def dose(self, speed, timeout=0.1):
        """Pulse the pump for timeout seconds.
        :param timeout: Timeout, in seconds, of the pump pulse
        :param blocking: If true, function will block until pump has stopped
        :param force: Applies only to non-blocking. If true, any previous dose will be replaced
        """
        print(f"Dose pump on GPIO pin {self._pin} at speed {speed} for {timeout} seconds.")
        if self.set_speed(speed):
            time.sleep(timeout)
            self.stop()
            return True

        return False
