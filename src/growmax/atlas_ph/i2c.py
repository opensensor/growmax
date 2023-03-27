import machine
import utime
from growmax.utils.mcu import i2c_channel_pins

import config


DEFAULT_ADDRESS = 0x63


class AtlasPHI2C:

    def __init__(self, i2c_channel=0):
        pin_scl, pin_sda = i2c_channel_pins(i2c_channel)
        i2c_channel_pins(i2c_channel)
        self.i2c_bus = machine.I2C(i2c_channel, scl=machine.Pin(pin_scl), sda=machine.Pin(pin_sda), freq=100000)

        if hasattr(config, "ATLAS_PH_METER_ADDRESS"):
            self.address = config.ATLAS_PH_METER_ADDRESS or DEFAULT_ADDRESS
        else:
            self.address = DEFAULT_ADDRESS

    def obtain_ph_reading(self):
        self.i2c_bus.writeto(self.address, 'R,\r'.encode())
        utime.sleep(1.0)
        data = self.i2c_bus.readfrom(self.address, 31)
        if data[0] == 1:  # Successful reading
            reading = data[1:].decode().strip('\x00')
        else:
            reading = None
            print("Unable to get reading--check Atlas Scientific pH device settings")
        return reading

