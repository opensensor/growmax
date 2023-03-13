
def i2c_channel_pins(i2c_channel=0):
    pin_scl = 1
    pin_sda = 0
    if i2c_channel == 1:
        pin_scl = 19
        pin_sda = 18
    return pin_scl, pin_sda
