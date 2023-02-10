import machine
import time
import config

display = None


def toggle_display(pin):
    global display
    if display:
        if pin.value():
            display.poweron()
        else:
            display.poweroff()


if config.DISPLAY:
    if config.DISPLAY == "SSD1327_I2C":
        from growmax.displays.ssd1327 import SSD1327_I2C

        scl = machine.Pin(1)
        sda = machine.Pin(0)
        if config.DISPLAY_I2C_CHANNEL == 1:
            scl = machine.Pin(19)
            sda = machine.Pin(18)
        i2c = machine.I2C(config.DISPLAY_I2C_CHANNEL, scl=scl, sda=sda, freq=100000)
        display = SSD1327_I2C(128, 128, i2c, addr=config.DISPLAY_I2C_ADDRESS)
    if config.DISPLAY_SWITCH:
        switch = machine.Pin(config.DISPLAY_SWITCH, machine.Pin.IN, config.DISPLAY_SWITCH_PULL)
        switch.irq(trigger=config.DISPLAY_SWITCH_TRIGGER, handler=toggle_display)


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
    display.poweron()
    micropython_logo()
    time.sleep(5.0)
    display.poweroff()
