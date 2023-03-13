from growmax.utils.mcu import get_gpio_for_mcu


def i2c_channel_pins(i2c_channel=0):
    pin_scl = 1
    pin_sda = 0
    if i2c_channel == 1:
        pin_scl = 19
        pin_sda = 18
    return get_gpio_for_mcu(pin_scl), get_gpio_for_mcu(pin_sda)
