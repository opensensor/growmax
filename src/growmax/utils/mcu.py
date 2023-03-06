import config

from growmax import constants


def get_gpio_for_mcu(rp2040_gpio):
    if getattr(config, "GROWMAX_MCU", None) and config.GROWMAX_MCU == "ESP32S3_BPI":
        return constants.RP2040_MCU_MAPPINGS["ESP32S3_BPI"][rp2040_gpio]
    return rp2040_gpio

