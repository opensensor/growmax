import machine
import time

import config
from growmax.utils.configs import get_config_value
from growmax.utils.mcu import i2c_channel_pins
from growmax.relays.i2c_relays import RelayBoard


def initialize_relay_board():
    if get_config_value("RELAY_BOARD_ENABLED"):
        i2c_channel = config.RELAY_BOARD_I2C_CHANNEL
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
            relay_board = RelayBoard(
                i2c,
                addr=config.RELAY_BOARD_I2C_ADDRESS,
                num_relays=config.RELAY_BOARD_NUM_RELAYS
            )
            return relay_board
        except Exception as e:
            print(e)
    return None
