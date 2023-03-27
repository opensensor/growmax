import config

from growmax import constants


def get_gpio_for_mcu(rp2040_gpio):
    if getattr(config, "GROWMAX_MCU", None) and config.GROWMAX_MCU == "ESP32S3_BPI":
        return constants.RP2040_MCU_MAPPINGS["ESP32S3_BPI"][rp2040_gpio]
    return rp2040_gpio

def i2c_channel_pins(i2c_channel=0):
    pin_scl = 1
    pin_sda = 0
    if i2c_channel == 1:
        pin_scl = 19
        pin_sda = 18
    return get_gpio_for_mcu(pin_scl), get_gpio_for_mcu(pin_sda)
