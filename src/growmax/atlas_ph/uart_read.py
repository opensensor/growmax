from machine import UART, Pin
import utime

# Device should be in UART mode for this script
# assumes you haven't changed the default baud rate of 9600
uart = UART(0, 9600, tx=Pin(0), rx=Pin(1))
uart.init(9600, bits=8, parity=None, stop=1)

utime.sleep(2.0)
while True:
    print(uart.readline())
    utime.sleep(1.0)
