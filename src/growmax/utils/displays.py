import gc
import machine
import time

from growmax.utils.mcu import get_gpio_for_mcu

import config


display = None


def toggle_display(pin):
    try:
        global display
        if display:
            if pin.value():
                display.poweron()
            else:
                display.poweroff()
    except Exception as e:
        print(e)


try:
    if config.DISPLAY:
        pin_scl = 1
        pin_sda = 0
        if config.DISPLAY_I2C_CHANNEL == 1:
            pin_scl = 19
            pin_sda = 18
        scl = machine.Pin(get_gpio_for_mcu(pin_scl))
        sda = machine.Pin(get_gpio_for_mcu(pin_sda))
        if config.DISPLAY == "SSD1327_I2C":
            from growmax.displays.ssd1327 import SSD1327_I2C
            i2c = machine.I2C(config.DISPLAY_I2C_CHANNEL, scl=scl, sda=sda, freq=100000)
            display = SSD1327_I2C(128, 128, i2c, addr=config.DISPLAY_I2C_ADDRESS)

        if config.DISPLAY == "SH1107_I2C":
            from growmax.displays.sh1107 import SH1107_I2C
            i2c = machine.I2C(config.DISPLAY_I2C_CHANNEL, scl=scl, sda=sda, freq=100000)
            display = SH1107_I2C(128, 128, i2c, addr=config.DISPLAY_I2C_ADDRESS)
        if config.DISPLAY_SWITCH:
            switch = machine.Pin(get_gpio_for_mcu(config.DISPLAY_SWITCH), machine.Pin.IN, config.DISPLAY_SWITCH_PULL)
            switch.irq(trigger=config.DISPLAY_SWITCH_TRIGGER, handler=toggle_display)
except Exception as exc:
    print(f"Exception trying to initialize display: {exc}")


def micropython_logo():
    global display
    x = (display.width - 69) // 2
    y = (display.height - 99) // 2
    display.framebuf.fill_rect(x + 0, y + 0, 69, 69, 15)
    display.framebuf.fill_rect(x + 15, y + 15, 3, 54, 0)
    display.framebuf.fill_rect(x + 33, y + 0, 3, 54, 0)
    display.framebuf.fill_rect(x + 51, y + 15, 3, 54, 0)
    display.framebuf.fill_rect(x + 60, y + 56, 4, 7, 0)
    display.text("Growmax by", 20, 90)
    display.text("OpenSensor.io", 10, 110)
    display.show()


def boot_sequence():
    global display
    if display:
        try:
            display.poweron()
            micropython_logo()
            time.sleep(5.0)
            display.poweroff()
        except Exception as e:
            print(e)


def display_basic_stats(has_water, pump_position, soil_moisture, moisture_config):
    global display
    if display:
        try:
            gc.collect()
            display.fill(0)
            display.text("Water ", 0, 0)
            display.text(str(has_water), 64, 0)
            display.text("P ", 0, 20)
            display.text(pump_position, 9, 20)
            display.text("Reads: ", 22, 20)
            display.text(str(soil_moisture), 64, 20)
            display.text("Config:", 0, 40)
            display.text(str(moisture_config), 64, 40)
            display.show()
            gc.collect()
        except Exception as e:
            print(e)


def display_ph_reading(ph_reading):
    global display
    print(ph_reading)
    if display:
        try:
            gc.collect()
            display.fill(0)
            display.text("pH ", 0, 0)
            display.text(str(ph_reading), 64, 0)
            display.show()
            gc.collect()
        except Exception as e:
            print(e)


def display_scd4x_reading(temp, rh, ppm_carbon_dioxide):
    global display
    print("Temperature: %0.1f *C" % temp)
    print("Humidity: %0.1f %%" % rh)
    print("CO2: %d ppm" % ppm_carbon_dioxide)
    if display:
        try:
            gc.collect()
            display.fill(0)
            display.text("temp ", 0, 0)
            display.text(str(temp), 64, 0)
            display.text("rh ", 0, 32)
            display.text(str(rh), 64, 32)
            display.text("CO2 ppm ", 0, 64)
            display.text(str(ppm_carbon_dioxide), 64, 64)
            display.show()
            gc.collect()
        except Exception as e:
            print(e)
