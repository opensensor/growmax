import machine
import time
from growmax.sensors import adafruit_scd4x
from growmax.utils.mcu import i2c_channel_pins


def init_adafruit_scd4x(i2c_channel=0):
    pin_scl, pin_sda = i2c_channel_pins(i2c_channel)
    try:
        time.sleep(2.0)
        i2c = machine.I2C(
            i2c_channel,
            scl=machine.Pin(pin_scl),
            sda=machine.Pin(pin_sda),
            freq=100000
        )
        time.sleep(2.0)
        scd4x = adafruit_scd4x.SCD4X(i2c)
        time.sleep(2.0)
        print("Serial number:", [hex(i) for i in scd4x.serial_number])
        time.sleep(1.0)
        scd4x.start_periodic_measurement()
        print("Waiting for first measurement....")
        time.sleep(1.0)
        return scd4x
    except Exception as e:
        print(e)
    return None


def read_adafruit_scd4x(scd4x):
    time.sleep(2.0)
    if scd4x.data_ready:
        ppm_carbon_dioxide = scd4x.CO2
        temp = scd4x.temperature
        rh = scd4x.relative_humidity
        return [temp, rh, ppm_carbon_dioxide]
    print("SCD-40 data not available")
    return [None, None, None]
